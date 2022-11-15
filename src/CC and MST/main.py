import Graph as g


def main():

    adj_matrix = g.random_adj_matrix(4)
    graph = g.Graph(adj_matrix)

    print(graph)


if __name__ == "__main__":
    main()
