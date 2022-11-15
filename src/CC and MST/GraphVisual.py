import networkx as nx
import matplotlib.pyplot as plt


class GraphVisual:

    def __init__(self, graph):
        self.graph = nx.Graph(graph)

    def get_nodes(self):
        return self.graph.nodes

    def visualize(self):
        nx.draw_networkx(self.graph)
        plt.show()
