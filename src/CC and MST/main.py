import Graph as g
import GraphVisual as gv

# --- Costanti per testing --- #
NUM_NODES = 4
EDGE_PROBABILITY = 0.50
DIRECTED = False    # per avere o meno le frecce
SAVE_TO_FILE = True    # salva png grafo e info su .txt


# FIXME: quando si sovrappongono due archi non mostra i due pesi diversi!

def main():
    adj_matrix = g.random_adj_matrix(NUM_NODES,
                                     EDGE_PROBABILITY,  # di default la probabilità di avere un arco è del 50%
                                     DIRECTED)
    graph = g.Graph(adj_matrix)

    # Aggiungo un nodo ed un arco random
    # graph.add_node("X")
    # graph.add_edge(("X", "A"))

    print(graph)

    graph_visual = gv.GraphVisual(graph.get_graph_dict(), adj_matrix, DIRECTED)
    graph_visual.visualize(graph.weights(), SAVE_TO_FILE)

    if SAVE_TO_FILE:
        gv.save_to_file(graph.__str__())

    graph.SCC()     # FIXME: un po' buggato


if __name__ == "__main__":
    main()
