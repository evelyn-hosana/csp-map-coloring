"""
chromatic.py - chromatic number computation.

finds minimum k such that valid k-coloring exists for given map. uses solve_dfs_fc_singleton for efficiency.
expected: Australia chi = 3, USA chi = 4.
"""

# TODO: define compute_chromatic_number(adjacency) -> tuple[int, dict]
# - import CSP and solve_dfs_fc_singleton
# - iterate k = 1, 2, 3, ...
# - build CSP with k colors; call solve_dfs_fc_singleton
# - if solution found, return (k, solution)
# - worst case: return (len(adjacency), {})
