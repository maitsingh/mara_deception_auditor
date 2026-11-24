"""Reproduce exploratory results. Run from repository root: python analysis/behavior.py.

Requires numpy. No model calls. Source classifications are not manually revalidated.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ARMS = ['off_switch', 'placebo', 'on_switch']

def analyze():
    with (ROOT / 'data/source/game_metrics.csv').open() as handle:
        rows = list(csv.DictReader(handle))
    by_seed = {arm: defaultdict(list) for arm in ARMS}
    results = {'status': 'exploratory', 'classification_validation': 'not independently completed', 'arms': {}}
    for arm in ARMS:
        group = [r for r in rows if r['arm'] == arm]
        totals = {k: sum(int(r[k]) for r in group) for k in [
            'hand_statements_false_before', 'hand_statements_checked_before',
            'hand_statements_false_after', 'hand_statements_checked_after']}
        deltas = []
        for r in group:
            nb, na = int(r['hand_statements_checked_before']), int(r['hand_statements_checked_after'])
            if min(nb, na) == 0:
                raise ValueError('Specify zero-denominator handling before analysis')
            delta = int(r['hand_statements_false_after']) / na - int(r['hand_statements_false_before']) / nb
            by_seed[arm][int(r['seed'])].append(delta)
            deltas.append(delta)
        eligible = [r for r in group if r['counted_in_test'] == '1']
        results['arms'][arm] = dict(totals, games=len(group),
            mean_game_change_pp=100 * float(np.mean(deltas)),
            eligible_games=len(eligible),
            mean_checkable_before=float(np.mean([float(r['checkable_per_turn_before']) for r in eligible])),
            mean_checkable_after=float(np.mean([float(r['checkable_per_turn_after']) for r in eligible])))
    seed_sets = [set(by_seed[a]) for a in ARMS]
    if not all(s == seed_sets[0] for s in seed_sets):
        raise ValueError('Unequal seed coverage')
    seeds = sorted(seed_sets[0])
    means = {a: np.array([np.mean(by_seed[a][s]) for s in seeds]) for a in ARMS}
    rng = np.random.default_rng(20261123)
    draws = rng.integers(0, len(seeds), (20000, len(seeds)))
    results['matched_seed_comparisons'] = {}
    for arm in ['off_switch', 'on_switch']:
        difference = means[arm] - means['placebo']
        interval = np.quantile(difference[draws].mean(axis=1)*100, [.025, .975])
        results['matched_seed_comparisons'][arm] = {
            'estimate_pp': float(difference.mean()*100), 'interval_pp': interval.tolist()}
    results['bootstrap'] = {'seed_blocks': len(seeds), 'resamples': 20000, 'random_seed': 20261123,
        'method': 'percentile bootstrap over matched seed blocks; seeds equally weighted',
        'multiplicity_adjustment': 'none; exploratory'}
    return results

if __name__ == '__main__':
    results = analyze()
    (ROOT/'results/behavior.json').write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))
