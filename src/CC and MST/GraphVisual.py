import networkx as nx
import matplotlib.pyplot as plt
import json


def save_to_file(graph):
    with open('graph.txt', 'w') as convert_file:
        convert_file.write(json.dumps(graph))


class GraphVisual:

    def __init__(self, graph, adj_matrix):
        self.graph = nx.Graph(graph)
        self.matrix = adj_matrix

    def get_nodes(self):
        return self.graph.nodes

    def visualize(self, weights, save=False):
        pos = nx.spring_layout(self.graph)

        nx.draw(self.graph, pos, with_labels=True, node_size=900, node_color="tab:green")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights, font_size=20)

        if save:

            plt.savefig("graph.png")

        plt.show()
