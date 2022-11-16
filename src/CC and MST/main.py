import Graph as g
import GraphVisual as gv

# --- Costanti per testing --- #
NUM_NODES = 5
EDGE_PROBABILITY = 0.50


def main():
    adj_matrix = g.random_adj_matrix(NUM_NODES,
                                     EDGE_PROBABILITY)  # di default la probabilità di avere un arco è del 50%
    graph = g.Graph(adj_matrix)

    # Aggiungo un nodo ed un arco random
    # graph.add_node("X")
    # graph.add_edge(("X", "A"))

    print(graph)

    graph_visual = gv.GraphVisual(graph.get_graph_dict(), adj_matrix)
    graph_visual.visualize(graph.weights())

if __name__ == "__main__":
    main()
