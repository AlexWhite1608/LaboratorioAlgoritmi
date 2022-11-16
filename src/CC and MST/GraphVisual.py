import networkx as nx
import matplotlib.pyplot as plt


class GraphVisual:

    def __init__(self, graph, adj_matrix):
        self.graph = nx.Graph(graph)
        self.matrix = adj_matrix

    def get_nodes(self):
        return self.graph.nodes

    def visualize(self, weights, save=False):
        pos = nx.spring_layout(self.graph)

        nx.draw(self.graph, pos, with_labels=True)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights, font_size=10)
        #nx.draw_networkx(self.graph, with_labels=True)

        if save:
            plt.savefig("graph.png")

        plt.show()
