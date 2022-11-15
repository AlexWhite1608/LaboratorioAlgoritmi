import numpy as np
from random import randint, choices


# Genera una matrice di adiacenza random forniti il numero di nodi n_nodes
def random_adj_matrix(n_nodes):
    array = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]
    values = [0, 1]

    for j in range(n_nodes):
        for i in range(n_nodes):
            probability = [randint(0, 100) / 100,
                           randint(0, 100) / 100]  # ad ogni cella ho una certa probabilità di avere 0 o 1
            array[j][i] = choices(values, probability)[0]
    return array


def matrix_to_graph_dict(adj_matrix):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Z"]
    dictionary = {}
    graph = {}

    for i in range(len(alphabet)):
        dictionary[i] = alphabet[i]

    for m in range(len(adj_matrix)):
        graph[dictionary[m]] = []
        for n in range(len(adj_matrix)):
            if adj_matrix[m][n] == 1:
                graph[dictionary[m]].append(dictionary[n])

    return graph


class Graph:
    def __init__(self, adj_matrix):
        self._matrix = adj_matrix
        self._graph = matrix_to_graph_dict(adj_matrix)

    def add_node(self, node):
        if node not in self._graph:
            self._graph[node] = []

    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self._graph:
            self._graph[node1].append(node2)
        else:
            self._graph[node1] = [node2]

    def nodes(self):
        return list(self._graph.keys())

    def edges(self):
        edges = []
        for node in self._graph:
            for neighbour in self._graph[node]:
                if (neighbour, node) not in edges:
                    edges.append((node, neighbour))
        return edges

    def __str__(self):
        res ="Matrice: " + str(self._matrix)
        res += "\nGrafo: " + str(self._graph)
        res += "\nNodi: "
        for node in self.nodes():
            res += str(node) + " "
        res += "\nArchi: "
        for edge in self.edges():
            res += str(edge) + " "
        return res
