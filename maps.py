"""
maps.py - adjacency definitions for CSP map coloring.

AUSTRALIA and USA defined as symmetric dicts (region/state -> list of neighbors).
AK and HI included as isolated nodes, same as Tasmania in AUSTRALIA.

usage:
    from maps import AUSTRALIA, USA, validate_adjacency
    validate_adjacency(AUSTRALIA)
    validate_adjacency(USA)
"""

# Lecture 6a - Slide 4 (map coloring as CSP example)
# Australia - 7 regions, SA borders 5 others (forces chi = 3)
AUSTRALIA = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'Q'],
    'Q':   ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':   ['NSW', 'SA'],
    'SA':  ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T':   [], # Tasmania - isolated, no neighbors
}

# USA - 50 states (chi = 4 per four-color theorem)
# AK and HI isolated, no contiguous neighbors
USA = {
    'AL': ['MS', 'TN', 'GA', 'FL'],
    'AK': [], # isolated, no contiguous neighbors
    'AZ': ['CA', 'NV', 'UT', 'CO', 'NM'],
    'AR': ['MO', 'TN', 'MS', 'LA', 'TX', 'OK'],
    'CA': ['OR', 'NV', 'AZ'],
    'CO': ['WY', 'NE', 'KS', 'OK', 'NM', 'AZ', 'UT'],
    'CT': ['NY', 'MA', 'RI'],
    'DE': ['MD', 'PA', 'NJ'],
    'FL': ['AL', 'GA'],
    'GA': ['FL', 'AL', 'TN', 'NC', 'SC'],
    'HI': [], # isolated, no contiguous neighbors
    'ID': ['WA', 'OR', 'NV', 'UT', 'WY', 'MT'],
    'IL': ['WI', 'IA', 'MO', 'KY', 'IN'],
    'IN': ['IL', 'MI', 'OH', 'KY'],
    'IA': ['MN', 'WI', 'IL', 'MO', 'NE', 'SD'],
    'KS': ['NE', 'CO', 'OK', 'MO'],
    'KY': ['IN', 'OH', 'WV', 'VA', 'TN', 'MO', 'IL'],
    'LA': ['TX', 'AR', 'MS'],
    'ME': ['NH'],
    'MD': ['PA', 'DE', 'WV', 'VA'],
    'MA': ['NH', 'VT', 'NY', 'CT', 'RI'],
    'MI': ['WI', 'IN', 'OH'],
    'MN': ['ND', 'SD', 'IA', 'WI'],
    'MS': ['LA', 'AR', 'TN', 'AL'],
    'MO': ['IA', 'IL', 'KY', 'TN', 'AR', 'OK', 'KS', 'NE'],
    'MT': ['ID', 'WY', 'SD', 'ND'],
    'NE': ['SD', 'IA', 'MO', 'KS', 'CO', 'WY'],
    'NV': ['OR', 'ID', 'UT', 'AZ', 'CA'],
    'NH': ['VT', 'MA', 'ME'],
    'NJ': ['NY', 'PA', 'DE'],
    'NM': ['AZ', 'CO', 'OK', 'TX'],
    'NY': ['PA', 'NJ', 'CT', 'MA', 'VT'],
    'NC': ['VA', 'TN', 'GA', 'SC'],
    'ND': ['MT', 'SD', 'MN'],
    'OH': ['MI', 'PA', 'WV', 'KY', 'IN'],
    'OK': ['CO', 'KS', 'MO', 'AR', 'TX', 'NM'],
    'OR': ['WA', 'ID', 'NV', 'CA'],
    'PA': ['NY', 'NJ', 'DE', 'MD', 'WV', 'OH'],
    'RI': ['CT', 'MA'],
    'SC': ['NC', 'GA'],
    'SD': ['ND', 'MT', 'WY', 'NE', 'IA', 'MN'],
    'TN': ['KY', 'VA', 'NC', 'GA', 'AL', 'MS', 'AR', 'MO'],
    'TX': ['NM', 'OK', 'AR', 'LA'],
    'UT': ['ID', 'WY', 'CO', 'AZ', 'NV'],
    'VT': ['NY', 'NH', 'MA'],
    'VA': ['WV', 'MD', 'NC', 'TN', 'KY'],
    'WA': ['ID', 'OR'],
    'WV': ['OH', 'PA', 'MD', 'VA', 'KY'],
    'WI': ['MN', 'MI', 'IL', 'IA'],
    'WY': ['MT', 'ID', 'UT', 'CO', 'NE', 'SD'],
}

# asserts adjacency dict is symmetric: raises AssertionError if any edge A->B is missing its reverse B->A
def validate_adjacency(adj: dict) -> None:
    for region, neighbors in adj.items():
        for n in neighbors:
            assert n in adj, f"unknown region: '{n}'"
            assert region in adj[n], f"asymmetric edge: {region} -> {n}"
