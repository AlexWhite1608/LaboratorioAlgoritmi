import Graph as g
import GraphVisual as gv


def main():
    adj_matrix = g.random_adj_matrix(5)  # di default la probabilità di avere un arco è del 50%
    graph = g.Graph(adj_matrix)

    # Aggiungo un nodo ed un arco random
    # graph.add_node("X")
    # graph.add_edge(("X", "A"))

    print(graph)

    graph_visual = gv.GraphVisual(graph.get_graph_dict())
    graph_visual.visualize()


if __name__ == "__main__":
    main()
