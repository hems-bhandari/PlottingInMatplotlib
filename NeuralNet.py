import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the layers of the neural network
layers = [4, 5, 2]

# Create a directed graph
G = nx.DiGraph()

# Add nodes for each layer
for i, layer in enumerate(layers):
    for j in range(layer):
        node_name = f"layer {i+1}\nnode {j+1}"
        G.add_node(node_name, subset=i+1)

# Add edges between nodes in adjacent layers
for i in range(len(layers) - 1):
    for j in range(layers[i]):
        for k in range(layers[i+1]):
            from_node = f"layer {i+1}\nnode {j+1}"
            to_node = f"layer {i+2}\nnode {k+1}"
            weight = round(0.1*(j+1), 2)
            G.add_edge(from_node, to_node, weight=weight)

# Set the position of nodes using the circular layout
pos = nx.circular_layout(G, scale=1.5)

# Draw the nodes with a different color palette
node_color = np.array([G.nodes[n]['subset'] for n in G.nodes()])
cmap = plt.cm.get_cmap('Set2', len(layers))
nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_color, cmap=cmap, alpha=0.9)

# Draw the labels for nodes
node_labels = {n: n.split('\n')[1] for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_weight='bold', font_color='w')

# Draw the edges with a color map based on edge weights
edge_weights = [G.edges[e]['weight'] for e in G.edges()]
edge_color = [cmap(float(w)) for w in edge_weights]
nx.draw_networkx_edges(G, pos, width=2, edge_color=edge_color, arrowsize=20)

# Add labels to the edges
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3)

# Set the plot style
plt.style.use('seaborn')

# Remove the axis and grid lines
plt.axis('off')
plt.grid(None)

# Add a color bar to show the mapping of subset to color
sm = plt.cm.ScalarMappable(cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm, ticks=np.arange(len(layers))+0.5)
cbar.ax.set_yticklabels([f'Layer {i+1}' for i in range(len(layers))])
cbar.ax.tick_params(labelsize=12)

# Show the plot
plt.show()
