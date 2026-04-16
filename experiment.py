"""
experiment.py - trial runner, stats collection, and results table printer.

without heuristics: all 3 algorithms share same random variable order per trial.
with heuristics: MRV+DH determines order at runtime.

each trial records backtrack count and wall-clock time via time.perf_counter().
"""
NUM_TRIALS = 5 # default trial count; overridden by --trials CLI arg

# TODO: define run_single(adjacency, num_colors, variable_order, solver_fn) -> dict
# - create and reset CSP with given order and num_colors
# - time solver call with time.perf_counter()
# - return {'backtracks': int, 'time_sec': float, 'solution': dict | None}

# TODO: define run_experiment(adjacency, num_colors, map_name, num_trials) -> dict
# without heuristics loop (num_trials iterations):
# - shuffle variable list once; pass same order to solve_dfs, solve_dfs_fc, solve_dfs_fc_singleton
# with heuristics loop (num_trials iterations):
# - shuffle variable list; run solve_dfs_heuristic, solve_dfs_fc_heuristic, solve_dfs_fc_singleton_heuristic
# - return structured results dict keyed by section and algorithm name

# TODO: define print_results_table(results)
# - print map name and k
# - for each section (no heuristics / heuristics):
# - for each algorithm: print BT row and time row across all trials + average
