"""
maps.py - adjacency definitions for CSP map coloring.

AUSTRALIA and USA defined as symmetric dicts (region/state -> list of neighbors).
Tasmania, Alaska, and Hawaii are modeled as isolated nodes 
because they have no land-border neighbors in this representation.

usage:
    from maps import AUSTRALIA, USA
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

# Approximate geographic positions (normalised 0–1) for graph drawing
AUSTRALIA_POS = {
    'WA':  (0.18, 0.50), 'NT':  (0.42, 0.72), 'SA':  (0.48, 0.43),
    'Q':   (0.68, 0.68), 'NSW': (0.70, 0.38), 'V':   (0.65, 0.22),
    'T':   (0.65, 0.07),
}

USA_POS = {
    'WA': (0.09,0.88), 'OR': (0.09,0.78), 'CA': (0.07,0.60),
    'ID': (0.19,0.82), 'NV': (0.15,0.66), 'AZ': (0.21,0.50),
    'MT': (0.30,0.90), 'WY': (0.30,0.79), 'UT': (0.23,0.68),
    'CO': (0.31,0.64), 'NM': (0.27,0.52),
    'ND': (0.44,0.91), 'SD': (0.44,0.83), 'NE': (0.44,0.74),
    'KS': (0.44,0.65), 'OK': (0.44,0.56), 'TX': (0.39,0.43),
    'MN': (0.55,0.91), 'IA': (0.56,0.79), 'MO': (0.56,0.69),
    'AR': (0.56,0.58), 'LA': (0.55,0.47),
    'WI': (0.63,0.87), 'IL': (0.63,0.74), 'KY': (0.66,0.63),
    'TN': (0.65,0.56), 'MS': (0.62,0.49), 'AL': (0.63,0.43),
    'MI': (0.70,0.84), 'IN': (0.68,0.73), 'OH': (0.74,0.73),
    'WV': (0.77,0.66), 'VA': (0.80,0.64), 'NC': (0.82,0.57),
    'SC': (0.82,0.50), 'GA': (0.74,0.47), 'FL': (0.74,0.36),
    'PA': (0.80,0.74), 'NY': (0.84,0.81), 'MD': (0.83,0.68),
    'DE': (0.85,0.71), 'NJ': (0.86,0.74), 'CT': (0.88,0.78),
    'RI': (0.90,0.79), 'MA': (0.88,0.83), 'VT': (0.87,0.87),
    'NH': (0.88,0.89), 'ME': (0.91,0.93),

    'AK': (0.05,0.12), # Alaska - isolated, no contiguous neighbors
    'HI': (0.20,0.08), # Hawaii - isolated, no contiguous neighbors
}
