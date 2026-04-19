"""
chromatic.py - chromatic number computation

finds minimum k such that valid k-coloring exists for given map. uses solve_dfs_fc_singleton for efficiency
expected: Australia chi = 3, USA chi = 4
"""
from csp import MapColoringCSP
from algorithms import solve_dfs_fc_singleton

def compute_chromatic_number(adjacency: dict) -> tuple[int, dict]:
    """Finds minimum k such that a valid k-coloring exists. Returns (k, solution)"""
    colors_pool = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
    variable_order = list(adjacency.keys())

    for k in range(1, len(adjacency) + 1):
        colors = colors_pool[:k]
        csp = MapColoringCSP(adjacency, colors)
        solution = solve_dfs_fc_singleton(csp, variable_order)
        if solution is not None: return (k, solution)
    return (len(adjacency), {})