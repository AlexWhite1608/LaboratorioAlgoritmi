from collections import defaultdict

import numpy as np
from random import randint, choices

RANGE_WEIGHT = 10


# Genera una matrice di adiacenza random forniti il numero di nodi n_nodes
def random_adj_matrix(n_nodes, p_edge=0.5):
    array = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]
    values = [x for x in range(RANGE_WEIGHT)]
    probability = []

    for x in values:
        if x > 0:
            probability.append(p_edge)
        else:
            probability.append(1 - p_edge)

    for j in range(n_nodes):
        for i in range(n_nodes):
            if i != j:    # PER TOGLIERE I SELF LOOP!
                array[j][i] = choices(values, probability)[0]
                array[i][j] = choices([array[j][i], 0], [p_edge, 1-p_edge])[0]  # Gestione frecce per avere grafo orientato con direzione random
    return array


def matrix_to_graph_dict(adj_matrix):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Z"]
    dictionary = {}
    graph = {}

    # inizializza il dizionario di supporto
    for i in range(len(alphabet)):
        dictionary[i] = alphabet[i]

    for m in range(len(adj_matrix)):
        graph[dictionary[m]] = {}
        for n in range(len(adj_matrix)):
            if adj_matrix[m][n] > 0:
                graph[dictionary[m]][dictionary[n]] = dictionary[n]
                graph[dictionary[m]][dictionary[n]] = adj_matrix[m][n]

    return graph


class Graph:
    def __init__(self, adj_matrix):
        self._matrix = adj_matrix
        self._graph = matrix_to_graph_dict(adj_matrix)

    # FIXME: fix alle strutture dati (da lista a dict)
    def add_node(self, node):  # TODO: si deve modificare anche la matrice!
        if node not in self._graph:
            self._graph[node] = []

    def add_edge(self, edge):  # TODO: si deve modificare anche la matrice!
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self._graph:
            self._graph[node1].append(node2)
        else:
            self._graph[node1] = [node2]

    def get_graph_dict(self):
        return self._graph

    def nodes(self):
        return list(self._graph.keys())

    def edges(self):
        edges = []
        for node in self._graph:
            for neighbour in self._graph[node]:
                if (neighbour, node) not in edges:
                    edges.append((node, neighbour))
        return edges

    def weights(self):
        weights = {}

        for k, v in self._graph.items():
            for x, y in v.items():
                (k, x) = tuple([k, x])
                if (x, k) not in weights:   # rimuove archi duplicati del tipo (A, B) = (B, A)
                    weights[(k, x)] = y

        return weights

    def __str__(self):
        res = "Matrice: " + str(self._matrix)
        res += "\nGrafo: " + str(self._graph)
        res += "\nNodi: "
        for node in self.nodes():
            res += str(node) + " "
        res += "\nArchi: "
        for edge in self.edges():
            res += str(edge) + " "
        res += "\nPesi: " + str(self.weights())
        return res
