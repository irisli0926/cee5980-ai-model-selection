"""Audit candidate eligibility and the exact clarification feasibility boundary."""
import json
from decimal import Decimal

import numpy as np
import pandas as pd

from analysis import (
    BASE, FIELDS, PROFILES, SCREEN, WORKFLOWS, load_data, nondominated, plt,
    preference_grid, value_matrix,
)


GLM = 'GLM-4.6 (FC thinking)'
FLAGGED = {'Ministral-8B-Instruct-2410 (FC)', 'Llama-3.1-Nemotron-Ultra-253B-v1 (FC)'}
TOLERANCE = 1e-12


def describe_scenario(data, workflow, anchors, baseline_pareto):
    objectives = np.column_stack((data[workflow], data.avoidance, -data.benchmark_cost, -data.p95_latency))
    pareto = nondominated(objectives)
    pareto_ids = set(data.loc[pareto, 'model'])
    # Independent scalar check on the raw oriented consequences.
    points = objectives.tolist()
    scalar_front = {
        model for model, point in zip(data.model, points)
        if not any(all(other >= current for other, current in zip(row, point)) and row != point
                   for row in points)
    }
    assert pareto_ids == scalar_front
    feasible = (data[workflow].ge(SCREEN['performance_min']) & data.avoidance.ge(SCREEN['avoidance_min']) &
                data.benchmark_cost.le(SCREEN['benchmark_cost_max']) & data.p95_latency.le(SCREEN['p95_latency_max']))
    values = value_matrix(data, workflow, anchors)
    assert np.isfinite(values).all() and ((0 <= values) & (values <= 1)).all()
    winners = {}
    for profile, weights in PROFILES.items():
        score = values @ weights
        winners[profile] = sorted(data.loc[np.isclose(score, score.max(), rtol=0, atol=TOLERANCE), 'model'])
        assert set(winners[profile]) <= pareto_ids
    balanced = values @ PROFILES['balanced']
    shortlist = sorted(data.loc[feasible, 'model'])
    screened_winners = []
    if shortlist:
        screened_winners = sorted(data.loc[feasible & np.isclose(
            balanced, balanced[feasible].max(), rtol=0, atol=TOLERANCE), 'model'])
    frontier_values = values[pareto] @ preference_grid().T
    coverage = np.isclose(frontier_values, frontier_values.max(axis=0), rtol=0, atol=TOLERANCE).any(axis=1)
    return {
        'pareto_models': sorted(pareto_ids),
        'pareto_gains': sorted(pareto_ids - baseline_pareto),
        'pareto_losses': sorted(baseline_pareto - pareto_ids),
        'feasible_models': shortlist,
        'illustrative_profile_winners': winners,
        'balanced_winners_after_screen': screened_winners,
        'pareto_models_optimal_on_weight_grid': sorted(data.loc[pareto, 'model'].to_numpy()[coverage]),
    }


def clarification_boundary(data):
    """Emit strict increases in achievable clarification as the P95 ceiling grows."""
    pool = data.loc[data.avoidance.ge(SCREEN['avoidance_min']) & data.benchmark_cost.le(SCREEN['benchmark_cost_max'])]
    steps = []
    best = -1.0
    for latency, rows in pool.groupby('p95_latency', sort=True):
        score = float(rows.clarification.max())
        if score > best:
            best = score
            steps.append({'p95_ceiling_inclusive_s': float(latency), 'maximum_clarification_pct': score,
                          'models_at_jump': sorted(rows.loc[rows.clarification.eq(score), 'model'])})
    # Check both sides of every observed latency change and at the example limit.
    for limit in [SCREEN['p95_latency_max'], *pool.p95_latency, *np.nextafter(pool.p95_latency, -np.inf)]:
        observed = pool.loc[pool.p95_latency.le(limit), 'clarification']
        expected = None if observed.empty else float(observed.max())
        actual = next((x['maximum_clarification_pct'] for x in reversed(steps)
                       if x['p95_ceiling_inclusive_s'] <= limit), None)
        assert actual == expected
    return steps


def weighted_sum_example(data, baseline_pareto):
    target = 'GPT-4.1-2025-04-14 (FC)'
    pair = ['Claude-Haiku-4-5-20251001 (FC)', 'Gemini-2.5-Flash-Lite (FC)']
    fields = ['clarification', 'avoidance', 'benchmark_cost', 'p95_latency']
    selected = data.set_index('model').loc[[target, *pair], fields]
    point, first, second = [list(map(lambda x: Decimal(str(x)), row)) for row in selected.to_numpy()]
    midpoint = [(a + b) / 2 for a, b in zip(first, second)]
    assert set([target, *pair]) <= baseline_pareto
    assert all(m > p for m, p in zip(midpoint[:2], point[:2]))
    assert all(m < p for m, p in zip(midpoint[2:], point[2:]))
    return {'field_order': fields, 'target': target, 'target_consequences': list(map(float, point)),
            'witness_models': pair, 'witness_midpoint': list(map(float, midpoint))}


def draw_boundary(baseline, expanded, path):
    """Zoom to the requirement region where admitting GLM changes feasibility."""
    left = 5
    right = 22
    fig, ax = plt.subplots(figsize=(6.45, 3.0), layout='constrained')
    navy, orange = '#15546a', '#ad4e19'
    for label, steps, color, style in [('66-candidate baseline', baseline, navy, '-'),
                                      ('Also admit GLM-4.6', expanded, orange, '--')]:
        x = [row['p95_ceiling_inclusive_s'] for row in steps]
        y = [row['maximum_clarification_pct'] for row in steps]
        ax.step([*x, right], [*y, y[-1]], where='post', color=color, linestyle=style, lw=1.8, label=label)
    x = sorted({left, right, *(r['p95_ceiling_inclusive_s'] for r in [*baseline, *expanded]
                               if left < r['p95_ceiling_inclusive_s'] < right)})
    heights = [[max(r['maximum_clarification_pct'] for r in steps if r['p95_ceiling_inclusive_s'] <= limit)
                for limit in x] for steps in (baseline, expanded)]
    ax.fill_between(x, *heights, step='post', color=orange, alpha=0.12)
    p95, score = SCREEN['p95_latency_max'], SCREEN['performance_min']
    ax.scatter(p95, score, marker='X', s=45, color='#252732', zorder=5)
    ax.annotate(f'Illustrative screen\n{p95:g} s / {score:g}%', (p95, score), (15.45, 54.4), fontsize=8,
                arrowprops={'arrowstyle': '-', 'color': '#525560', 'lw': 0.8})
    labels = [('Claude-Opus-4-5-20251101 (FC)', 'Opus 4.5', navy), (GLM, 'GLM-4.6', orange),
              ('xLAM-2-32b-fc-r (FC)', 'xLAM-32B', navy)]
    for model, label, color in labels:
        step = next(r for r in [*baseline, *expanded] if model in r['models_at_jump'])
        x, y = step['p95_ceiling_inclusive_s'], step['maximum_clarification_pct']
        ax.scatter(x, y, s=16, color=color, zorder=5)
        ax.annotate(f'{label}\n{x:.2f} s / {y:g}%', (x, y), xytext=(1, 5), textcoords='offset points',
                    fontsize=8, color=color)
    ax.set(xlim=(left, right), ylim=(50, 74), xlabel='Allowed whole-benchmark P95 (seconds)',
           ylabel='Maximum clarification score (%)', xticks=(5, 8, 11, 15, 18, 22), yticks=(50, 55, 60, 65, 70))
    ax.tick_params(labelsize=8)
    ax.grid(alpha=0.18)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='upper left', frameon=False, fontsize=8)
    fig.savefig(path, dpi=260)
    plt.close(fig)


def run():
    raw, data, audit, manifest = load_data()
    summary = json.loads((BASE / 'results/summary.json').read_text())
    assert manifest['sha256'] == summary['source_sha256'] and len(data) == summary['eligible_configurations']
    anchors = summary['resource_value_anchors']
    row = audit.loc[audit.model.eq(GLM)].iloc[0]
    assert not row.included and row.valid_score_fields and row.positive_resource_fields and row.finite_fields
    glm = raw.loc[raw.Model.eq(GLM), list(FIELDS)].rename(columns=FIELDS).copy()
    for column in list(FIELDS.values())[1:]:
        glm[column] = pd.to_numeric(glm[column].astype(str).str.rstrip('%'))
    flagged = data.loc[data.model.isin(FLAGGED)]
    assert len(flagged) == 2 and flagged[['structured', 'clarification']].eq(0).all().all()
    assert flagged.avoidance.eq(100).all()
    without_flagged = data.loc[~data.model.isin(FLAGGED)]
    scenario_data = {
        'baseline': data,
        'admit_glm': pd.concat([data, glm], ignore_index=True),
        'omit_flagged': without_flagged,
        'both_changes': pd.concat([without_flagged, glm], ignore_index=True),
    }
    baseline_sets = {w: set(pd.read_csv(BASE / f'results/{w}_pareto_set.csv').model) for w in WORKFLOWS}
    scenarios = {}
    for name, candidates in scenario_data.items():
        scenarios[name] = {'candidate_count': len(candidates), 'workflows': {
            w: describe_scenario(candidates, w, anchors, baseline_sets[w]) for w in WORKFLOWS
        }, 'clarification_boundary': clarification_boundary(candidates)}
    for workflow, original in summary['workflows'].items():
        result = scenarios['baseline']['workflows'][workflow]
        assert set(result['pareto_models']) == baseline_sets[workflow]
        assert len(result['pareto_models']) == original['pareto_count']
        assert len(result['feasible_models']) == original['illustrative_screen_feasible_count']
        assert result['illustrative_profile_winners'] == original['profile_winners']
        assert result['balanced_winners_after_screen'] == original['illustrative_screen_winners']
    audit_result = {'source_sha256': manifest['sha256'], 'fixed_screen': SCREEN, 'fixed_linear_anchors': anchors,
                    'added_candidate': GLM, 'omitted_candidates': sorted(FLAGGED),
                    'weight_grid_step': 0.05, 'weight_grid_size': len(preference_grid()),
                    'scenarios': scenarios, 'clarification_weighted_sum_example':
                        weighted_sum_example(data, baseline_sets['clarification'])}
    (BASE / 'results/decision_robustness_audit.json').write_text(json.dumps(audit_result, indent=2) + '\n')
    draw_boundary(scenarios['baseline']['clarification_boundary'], scenarios['admit_glm']['clarification_boundary'],
                  BASE / 'figures/05_clarification_feasibility.png')


if __name__ == '__main__':
    run()
