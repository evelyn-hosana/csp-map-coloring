"""
visualize.py - graph visualization, called from main.py when --visualize is set

requires: pip install networkx matplotlib
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# softer palette - easier on the eyes against dark background
_COLOR_MAP = {
    'C1': '#e05c5c', # red
    'C2': '#5aab6e', # green
    'C3': '#5b8dd9', # blue
    'C4': '#e8c23a', # yellow
    'C5': '#e0874a', # orange
    'C6': '#9b6dd4', # purple
}
BG = '#1e1e2e'

def draw_colored_map(adjacency, coloring, title, output_name=None, output_dir='.', pos=None):
    """Draw map as colored graph and save to {output_dir}/{title}.png

    adjacency: region -> [neighbor, ...]
    coloring: region -> color string (e.g. 'C1')
    title: filename stem and plot title
    output_name: custom filename for the output image
    output_dir: directory to save PNG
    pos: region -> (x, y) for geographic layout
    """
    import networkx as nx
    import matplotlib.pyplot as plt
    
    G = nx.Graph()
    G.add_nodes_from(adjacency.keys())
    for node, neighbors in adjacency.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    node_colors = [_COLOR_MAP.get(coloring.get(node, ''), '#888888') for node in G.nodes()]
    if pos is None: pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(20, 12), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_title(title, fontsize=22, fontweight='bold', color='white', pad=18)

    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='#444466', width=1.5)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors, node_size=1600, edgecolors='white', linewidths=1.2)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=8, font_weight='bold', font_color='white')

    legend_handles = [
        mpatches.Patch(color='#5b8dd9', label='Blue'),
        mpatches.Patch(color='#5aab6e', label='Green'),
        mpatches.Patch(color='#e05c5c', label='Red'),
        mpatches.Patch(color='#e8c23a', label='Yellow'),
    ]

    ax.legend(
        handles=legend_handles,
        loc='lower center',
        bbox_to_anchor=(0.5, -0.03),
        ncol=4,
        frameon=True,
        facecolor=BG,
        edgecolor='white',
        labelcolor='white',
        fontsize=10
    )

    ax.axis('off')
    filename = output_name if output_name is not None else title
    filepath = os.path.join(output_dir, f'{filename}.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()