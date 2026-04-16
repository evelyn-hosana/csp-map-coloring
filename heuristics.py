"""
heuristics.py - variable and value ordering heuristics: called by algorithm variants when use_heuristics=True.

ordering: MRV -> degree constraint -> LCV.
"""

# Lecture 6a - Slide 23
# Lecture 6a - Slide 24
# TODO: define select_variable(csp, assignment, domains, use_heuristics) -> str
# without heuristics: return next variable in csp.variables order
# with heuristics:
# - MRV: pick variable with smallest remaining domain size
# - degree heuristic (tie-breaker): among MRV ties, pick variable with most unassigned neighbors

# Lecture 6a - Slide 25
# TODO: define order_values(csp, var, assignment, domains, use_heuristics) -> list
# without heuristics: return list(domains[var]) as-is
# with heuristics (LCV):
# - for each color, count how many neighbor domain values it eliminates
# - return colors sorted ascending by that count (least constraining first)
