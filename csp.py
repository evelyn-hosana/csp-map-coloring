"""
csp.py - CSP class for map coloring: central data structure used by all 6 algorithm variants

tracks variables, domains, adjacency, and backtrack counter
"""

# Lecture 6a - Slide 3
class MapColoringCSP:
    """Encapsulates the CSP for map coloring, including variables, domains, adjacency, and backtrack counter"""
    def __init__(self, adjacency: dict, colors: list):
        self.adjacency = adjacency
        self.colors = colors[:]
        self.variables = list(adjacency.keys())
        self.domains = {v: colors[:] for v in self.variables}
        self.backtracks = 0

    def reset(self, variable_order: list, colors: list):
        # Resets the CSP to its initial state with the given variable order and colors.
        self.backtracks = 0
        self.colors = colors[:]
        self.variables = variable_order[:]
        self.domains = {v: self.colors[:] for v in self.variables}

    def is_consistent(self, var: str, color: str, assignment: dict) -> bool:
        # Returns True if assigning 'color' to 'var' is consistent with the current 'assignment'.
        for neighbor in self.adjacency[var]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def get_domains(self) -> dict:
        # Returns a copy of the current domains for all variables.
        return {v: self.colors[:] for v in self.variables}
