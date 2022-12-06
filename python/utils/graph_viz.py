import matplotlib.pyplot as plt
import networkx as nx

# define the graphs as a list of dictionaries
graphs = [
    {
        0: [(1, 2), (3, 4)],  # edges from vertex 0
        1: [(2, 3)],          # edges from vertex 1
        2: [(1, 4)],          # edges from vertex 2
        3: [(2, 0)],          # edges from vertex 3
        4: [(2, 1)]           # edges from vertex 4
    },
    {
        0: [ (1, 2), (3, 4), (2, 3) ],  # edges from vertex 0
        1: [ (5, 4) ],                  # edges from vertex 1
        2: [ (1, 4), (2, 1) ],          # edges from vertex 2
        3: [ (2, 0), (4, 1) ],          # edges from vertex 3
        4: [ (2, 1), (3, 0) ]           # edges from vertex 4
    },
    # add more graphs here
]

# create a figure
fig, axes = plt.subplots(nrows=1, ncols=len(graphs), figsize=(4 * len(graphs), 4))

# iterate over the list of graphs
for i, graph in enumerate(graphs):
    # create a networkx graph
    G = nx.DiGraph()

    # add the edges to the graph
    for v1, edges in graph.items():
        for edge in edges:
            cost, v2 = edge
            G.add_edge(v1, v2, weight=cost)

    # compute a spring layout for the graph
    pos = nx.spring_layout(G)

    # draw node of graph
    nx.draw_networkx_nodes(G, pos, ax=axes[i])

    # draw node labels
    nx.draw_networkx_labels(G, pos, ax=axes[i])

    # draw the edges with arrows
    nx.draw_networkx_edges(G, pos, ax=axes[i], connectionstyle="arc3,rad=0.05")

    # draw edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, ax=axes[i], edge_labels=edge_labels, label_pos=.8, verticalalignment="center_baseline")


# show the graphs
plt.show()

