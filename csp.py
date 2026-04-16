"""
csp.py - CSP class for map coloring: central data structure used by all 6 algorithm variants.

tracks variables, domains, adjacency, and backtrack counter.
"""

# Lecture 6a - Slide 3
class CSP:
    # TODO: define __init__(self, adjacency, num_colors)
    # - store adjacency (never mutate during search)
    # - set variables = list(adjacency.keys())
    # - set domains = {v: list(range(num_colors)) for v in variables}
    # - set backtracks = 0

    # TODO: define reset(self, variable_order, num_colors)
    # - zero backtracks
    # - update num_colors, variables, domains for fresh trial

    # TODO: define is_consistent(self, var, color, assignment) -> bool
    # - return False if any neighbor in adjacency[var] holds same color in assignment
    # - return True otherwise

    # TODO: define get_unassigned(self, assignment) -> list
    # - return [v for v in self.variables if v not in assignment]
    pass
