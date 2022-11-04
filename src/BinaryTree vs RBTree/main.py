from BinarySearchTree import *
import numpy as np

# --- Costanti per testing --- #
NUM_VALUES = 5
START_RANGE = 1
END_RANGE = 10


def main():
    tree = BinarySearchTree()

    values = np.random.randint(START_RANGE, END_RANGE, NUM_VALUES)

    for v in values:
        tree.add_node(tree.get_root(), v)

    tree.print_inorder(tree.get_root())

    find_me = np.random.randint(START_RANGE, END_RANGE, 1)

    if tree.search(tree.get_root(), find_me) is True:
        print("Valore " + str(find_me[0].astype(int)) + " trovato!")
    else:
        print("Valore " + str(find_me[0].astype(int)) + " non trovato!")


if __name__ == "__main__":
    main()
