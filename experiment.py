"""
experiment.py - trial runner and markdown output writer

without heuristics: all 3 algorithms share same random variable order per trial
with heuristics: MRV+DH determines order at runtime

each trial records backtrack count and wall-clock time via time.perf_counter()
"""
import random
import time
import concurrent.futures
from csp import MapColoringCSP
from algorithms import (
    solve_dfs, solve_dfs_fc, solve_dfs_fc_singleton,
    solve_dfs_heuristic, solve_dfs_fc_heuristic, solve_dfs_fc_singleton_heuristic
)

# Lecture 3b - Slide 8: DFS is "not complete in infinite-depth spaces" and "can loop without repeated-state checking" 
# On large graphs like USA (50 nodes), plain DFS can run indefinitely
TRIAL_TIMEOUT = 30 # trials exceeding cieling are marked DNF
_DNF = 'DNF'

NUM_TRIALS = 5 # default; overridden by --trials CLI arg

_NO_H_SOLVERS = [
    ('DFS', solve_dfs),
    ('DFS + FC', solve_dfs_fc),
    ('DFS + FC + Singleton', solve_dfs_fc_singleton),
]

_H_SOLVERS = [
    ('DFS + H', solve_dfs_heuristic),
    ('DFS + FC + H', solve_dfs_fc_heuristic),
    ('DFS + FC + Singleton + H', solve_dfs_fc_singleton_heuristic),
]

def run_single(adjacency, num_colors, variable_order, solver_fn) -> dict:
    """ Run one solver with a timeout and return backtracks, time, and solution
    If the solver exceeds TRIAL_TIMEOUT seconds, returns DNF sentinels
    """
    colors = [f'C{i+1}' for i in range(num_colors)]
    csp = MapColoringCSP(adjacency, colors)
    t0 = time.perf_counter()

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(solver_fn, csp, variable_order)
    try:
        solution = future.result(timeout=TRIAL_TIMEOUT)
        elapsed = time.perf_counter() - t0
        executor.shutdown(wait=False)
        return {'backtracks': csp.backtracks, 'time_sec': elapsed, 'solution': solution, 'timed_out': False}
    except concurrent.futures.TimeoutError:
        elapsed = time.perf_counter() - t0
        executor.shutdown(wait=False)
        return {'backtracks': _DNF, 'time_sec': _DNF, 'solution': None, 'timed_out': True}

def run_experiment(adjacency, num_colors, map_name, num_trials=NUM_TRIALS, run_no_heuristics=True, run_heuristics=True) -> dict:
    """Run all selected algorithm variants for num_trials trials

    Without heuristics: one random shuffle per trial, shared across all 3 variants
    With heuristics: MRV+DH+LCV determine variable/value order at runtime; initial order is still shuffled to vary starting state
    """
    variables = list(adjacency.keys())
    results = {
        'map_name': map_name,
        'num_colors': num_colors,
        'no_heuristics': None,
        'heuristics': None,
    }

    if run_no_heuristics:
        print(f"[{map_name}] Running without heuristics - DFS, DFS+FC, DFS+FC+Singleton...")
        no_h = {name: {'backtracks': [], 'times': []} for name, _ in _NO_H_SOLVERS}
        for t in range(num_trials):
            order = variables[:]
            random.shuffle(order)
            for name, solver_fn in _NO_H_SOLVERS:
                print(f"  [{map_name}] trial {t+1}/{num_trials} - {name}...", end=' ', flush=True)
                r = run_single(adjacency, num_colors, order, solver_fn)
                if r['timed_out']: print(f"DNF (>{TRIAL_TIMEOUT}s)")
                else: print(f"bt={r['backtracks']} ({r['time_sec']:.3f}s)")
                no_h[name]['backtracks'].append(r['backtracks'])
                no_h[name]['times'].append(r['time_sec'])
        results['no_heuristics'] = no_h

    if run_heuristics:
        print(f"[{map_name}] Running with heuristics - DFS+H, DFS+FC+H, DFS+FC+Singleton+H...")
        h = {name: {'backtracks': [], 'times': []} for name, _ in _H_SOLVERS}
        for t in range(num_trials):
            order = variables[:]
            random.shuffle(order)
            for name, solver_fn in _H_SOLVERS:
                print(f"  [{map_name}] trial {t+1}/{num_trials} - {name}...", end=' ', flush=True)
                r = run_single(adjacency, num_colors, order, solver_fn)
                if r['timed_out']: print(f"DNF (>{TRIAL_TIMEOUT}s)")
                else: print(f"bt={r['backtracks']} ({r['time_sec']:.3f}s)")
                h[name]['backtracks'].append(r['backtracks'])
                h[name]['times'].append(r['time_sec'])
        results['heuristics'] = h
    return results

# markdown output
def write_results_md(all_results, filepath):
    """Write experiment results to markdown file"""
    lines = _build_md(all_results)
    with open(filepath, 'w', encoding='utf-8') as f: f.write('\n'.join(lines))

def _build_md(all_results):
    """Build markdown lines for full results document"""
    num_trials = _derive_num_trials(all_results)
    lines = ['# CSP Map Coloring - Experiment Results', '']

    for map_name, results in all_results.items():
        k = results['num_colors']
        lines += [f'## {map_name} - k = {k}', '']
        for section_key, section_label in [('no_heuristics', 'Without Heuristics'), ('heuristics', 'With Heuristics'),]:
            section = results.get(section_key)
            if not section: continue
            lines += [f'### {section_label}', '']
            lines += _md_section_tables(section, num_trials)
    return lines

def _md_section_tables(section, num_trials):
    """markdown lines for BT and Time tables for one section

    DNF entries (timed-out trials) are shown as 'DNF' and excluded from averages
    """
    trial_cols = ' | '.join(f'T{i+1}' for i in range(num_trials))
    sep = '|:---' + ('|---:' * (num_trials + 1)) + '|'

    lines = []
    for metric_label, key, fmt in [('Backtracks', 'backtracks', lambda v: str(v)), ('Time (seconds)', 'times',  lambda v: f'{v:.6f}'),]:
        lines += [f'#### {metric_label}', '']
        lines.append(f'| Algorithm | {trial_cols} | **Avg** |')
        lines.append(sep)
        for alg, data in section.items():
            vals = data[key]
            cells = ' | '.join('DNF' if v is _DNF else fmt(v) for v in vals)
            completed = [v for v in vals if v is not _DNF]
            if completed:
                avg = sum(completed) / len(completed)
                avg_fmt = f'{avg:.1f}' if key == 'backtracks' else f'{avg:.6f}'
                avg_str = f'**{avg_fmt}**' if len(completed) == len(vals) else f'**{avg_fmt}**\\*'
            else: avg_str = '**DNF**'
            lines.append(f'| {alg} | {cells} | {avg_str} |')
        lines.append('')
    return lines

def _derive_num_trials(all_results):
    for results in all_results.values():
        for section_key in ('no_heuristics', 'heuristics'):
            section = results.get(section_key)
            if section:
                first = next(iter(section.values()))
                return len(first['backtracks'])
    return 0
