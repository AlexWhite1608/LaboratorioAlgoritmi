from BinarySearchTree import *
import numpy as np

# --- Costanti per testing --- #
NUM_VALUES = 5
START_RANGE = 1
END_RANGE = 10


def main():
    tree = BinarySearchTree()

    # values = np.random.randint(START_RANGE, END_RANGE, NUM_VALUES)

    for v in range(END_RANGE):
        tree.add_node(tree.get_root(), v)

    tree.print_inorder(tree.get_root())

    find_me = np.random.randint(START_RANGE, END_RANGE, 1)

    if tree.find(tree.get_root(), find_me) is True:
        print("\nValore " + str(find_me[0].astype(int)) + " trovato!\n")
        tree.delete(tree.search(find_me))
        print(str(find_me[0].astype(int)), "eliminato!")
        print("- - - - - - - - - - ")
        tree.print_inorder(tree.get_root())
    else:
        print("\nValore " + str(find_me[0].astype(int)) + " non trovato!")


if __name__ == "__main__":
    main()
