import Graph as g
import GraphVisual as gv


def main():

    adj_matrix = g.random_adj_matrix(4)
    graph = g.Graph(adj_matrix)

    print(graph)

    graph_visual = gv.GraphVisual(graph.get_graph_dict())

    graph_visual.visualize()


if __name__ == "__main__":
    main()
