import Graph as g


def main():
    adj_matrix = g.random_adj_matrix(3)
    graph = g.matrix_to_graph_dict(adj_matrix)

    print("Matrice")
    print(adj_matrix)
    print("\nGrafo")
    print(graph)


if __name__ == "__main__":
    main()
