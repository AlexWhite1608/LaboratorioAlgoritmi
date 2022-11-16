import networkx as nx
import matplotlib.pyplot as plt


class GraphVisual:

    def __init__(self, graph):
        self.graph = nx.Graph(graph)

    def get_nodes(self):
        return self.graph.nodes

    def visualize(self, save=False):
        nx.draw_networkx(self.graph)

        if save:
            plt.savefig("graph.png")

        plt.show()
