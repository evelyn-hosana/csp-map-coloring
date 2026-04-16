"""
visualize.py - graph visualization: called from main.py when --visualize flag is set.

requires: pip install networkx matplotlib
"""
COLOR_NAMES = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

# TODO: define draw_colored_map(adjacency, coloring, title)
# - build networkx Graph from adjacency
# - map each node's color int to COLOR_NAMES
# - draw with nx.spring_layout(seed=42), with_labels=True, node_size=800
# - save to f"{title}.png" and call plt.show()
# - imports needed: networkx, matplotlib.pyplot
