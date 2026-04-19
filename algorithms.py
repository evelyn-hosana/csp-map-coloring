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
from heuristics import select_variable, order_values

# Lecture 6b - Slide 36
def forward_check(csp, assigned_var, color, domains) -> bool:
    # remove color from each unassigned neighbor's domain; return false on wipe-out
    for neighbor in csp.adjacency[assigned_var]:
        if neighbor in domains:
            if color in domains[neighbor]:
                domains[neighbor].remove(color)
            if not domains[neighbor]:
                return False
    return True

# Lecture 6b - Slide 47
def propagate_singletons(csp, domains, assignment) -> bool:
    # repeatedly force-assign singleton domains until stable; return false on wipe-out
    changed = True
    while changed:
        changed = False
        for var in list(domains.keys()):
            if len(domains[var]) == 1:
                forced_color = domains[var][0]
                for neighbor in csp.adjacency[var]:
                    if neighbor in domains:
                        if forced_color in domains[neighbor]:
                            domains[neighbor].remove(forced_color)
                            changed = True
                        if not domains[neighbor]:
                            return False
    return True

# Lecture 6a - Slide 26
# domains passed explicitly for deep-copy pattern; csp.backtracks incremented on each undo
def backtrack(csp, assignment, domains, use_heuristics, use_fc, use_singleton, result) -> bool:
    if len(assignment) == len(csp.variables):
        result[0] = assignment.copy()
        return True
    var = select_variable(csp, assignment, domains, use_heuristics)

    for color in order_values(csp, var, assignment, domains, use_heuristics):
        if not csp.is_consistent(var, color, assignment): continue
        assignment[var] = color
        new_domains = {v: d[:] for v, d in domains.items() if v != var}

        if use_fc and not forward_check(csp, var, color, new_domains):
            del assignment[var]
            csp.backtracks += 1
            continue

        if use_singleton and not propagate_singletons(csp, new_domains, assignment):
            del assignment[var]
            csp.backtracks += 1
            continue

        if backtrack(csp, assignment, new_domains, use_heuristics, use_fc, use_singleton, result): return True
        del assignment[var]
        csp.backtracks += 1
    return False

# Lecture 3b - Slide 8
def solve_dfs(csp, variable_order) -> dict | None:
    csp.reset(variable_order, csp.colors)
    result = [None]
    backtrack(csp, {}, csp.get_domains(), False, False, False, result)
    return result[0]

def solve_dfs_fc(csp, variable_order) -> dict | None:
    csp.reset(variable_order, csp.colors)
    result = [None]
    backtrack(csp, {}, csp.get_domains(), False, True, False, result)
    return result[0]

def solve_dfs_fc_singleton(csp, variable_order) -> dict | None:
    csp.reset(variable_order, csp.colors)
    result = [None]
    backtrack(csp, {}, csp.get_domains(), False, True, True, result)
    return result[0]

def solve_dfs_heuristic(csp, variable_order) -> dict | None:
    csp.reset(variable_order, csp.colors)
    result = [None]
    backtrack(csp, {}, csp.get_domains(), True, False, False, result)
    return result[0]

def solve_dfs_fc_heuristic(csp, variable_order) -> dict | None:
    csp.reset(variable_order, csp.colors)
    result = [None]
    backtrack(csp, {}, csp.get_domains(), True, True, False, result)
    return result[0]

def solve_dfs_fc_singleton_heuristic(csp, variable_order) -> dict | None:
    csp.reset(variable_order, csp.colors)
    result = [None]
    backtrack(csp, {}, csp.get_domains(), True, True, True, result)
    return result[0]