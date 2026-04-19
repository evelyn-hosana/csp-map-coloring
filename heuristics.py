"""
heuristics.py - variable and value ordering heuristics: called by algorithm variants when use_heuristics=True

ordering: MRV -> degree constraint -> LCV
"""
# Lecture 6a - Slide 23-24
def select_variable(csp, assignment, domains, use_heuristics) -> str:
    """Returns the next variable to assign"""
    unassigned = [v for v in csp.variables if v not in assignment]
    if not use_heuristics: return unassigned[0]

    # MRV: pick variable with fewest remaining domain values
    return min(
        unassigned,
        key=lambda v: (
            len(domains[v]),
            -sum(1 for n in csp.adjacency[v] if n not in assignment) # degree heuristic (tie-breaker): most unassigned neighbors
        )
    )

# Lecture 6a - Slide 25
def order_values(csp, var, assignment, domains, use_heuristics) -> list:
    """Returns ordered list of values to try for var"""
    if not use_heuristics: return list(domains[var])

    # LCV: sort colors by how many values they eliminate from unassigned neighbors (ascending)
    def count_eliminations(color):
        return sum(
            1 for n in csp.adjacency[var]
            if n not in assignment and color in domains[n]
        )
    return sorted(domains[var], key=count_eliminations)