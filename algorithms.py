"""
algorithms.py - all 6 CSP solver variants and inference functions.

all variants share one recursive backtracking skeleton (backtrack()).
boolean flags control variable selection, value ordering, and inference level.

without heuristics (fixed random order per trial):
    solve_dfs - DFS only, no inference
    solve_dfs_fc - DFS + forward checking
    solve_dfs_fc_singleton - DFS + forward checking + singleton propagation

with heuristics (MRV + degree heuristic + LCV at runtime):
    solve_dfs_heuristic
    solve_dfs_fc_heuristic
    solve_dfs_fc_singleton_heuristic
"""

# Lecture 6b - Slide 36
# TODO: define forward_check(csp, assigned_var, color, domains) -> bool
# - remove color from each unassigned neighbor's domain
# - return False immediately if any neighbor domain becomes empty (wipe-out)
# - return True if all neighbors still have at least one value

# Lecture 6b - Slide 47
# TODO: define propagate_singletons(csp, domains, assignment) -> bool
# - loop until no changes:
# - for each unassigned variable with exactly 1 value in domain:
#   - remove that forced color from all unassigned neighbors' domains
#   - return False if any neighbor domain becomes empty
# - return True when stable

# Lecture 6a - Slide 26
# domains passed explicitly for deep-copy pattern; csp.backtracks incremented on each undo
# TODO: define backtrack(csp, assignment, domains, use_heuristics, use_fc, use_singleton, result)
# 1. if assignment is complete, store in result[0] and return True
# 2. select next variable via select_variable() from heuristics.py
# 3. order values via order_values() from heuristics.py
# 4. for each color:
# - check is_consistent()
# - assign; deep-copy domains into new_domains
# - if use_fc: run forward_check(); skip on failure
# - if use_singleton: run propagate_singletons(); skip on failure
# - recurse; return True if successful
# - undo assignment; increment csp.backtracks

# Lecture 3b - Slide 8
# TODO: define solve_dfs(csp, variable_order) -> dict | None
# call backtrack() with use_heuristics=False, use_fc=False, use_singleton=False

# TODO: define solve_dfs_fc(csp, variable_order) -> dict | None
# call backtrack() with use_heuristics=False, use_fc=True, use_singleton=False

# TODO: define solve_dfs_fc_singleton(csp, variable_order) -> dict | None
# call backtrack() with use_heuristics=False, use_fc=True, use_singleton=True

# TODO: define solve_dfs_heuristic(csp, variable_order) -> dict | None
# call backtrack() with use_heuristics=True, use_fc=False, use_singleton=False

# TODO: define solve_dfs_fc_heuristic(csp, variable_order) -> dict | None
# call backtrack() with use_heuristics=True, use_fc=True, use_singleton=False

# TODO: define solve_dfs_fc_singleton_heuristic(csp, variable_order) -> dict | None
# call backtrack() with use_heuristics=True, use_fc=True, use_singleton=True
