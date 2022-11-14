from BinarySearchTree import *
from RedBlackTree import *
import numpy as np

# --- Costanti per testing --- #
NUM_VALUES = 5
START_RANGE = 1
END_RANGE = 10


def main():
    bst_tree = BinarySearchTree()
    rb_tree = RBTree()

    # values = np.random.randint(START_RANGE, END_RANGE, NUM_VALUES)

    for v in range(END_RANGE):
        bst_tree.insert(v)
        rb_tree.insert(v)

    print("Binary Search Tree:")
    bst_tree.print_inorder(bst_tree.get_root())

    find_me = np.random.randint(START_RANGE, END_RANGE, 1)

    # Ricerca ed eliminazione valore nel BST
    if bst_tree.find(bst_tree.get_root(), find_me) is True:
        print("\nValore " + str(find_me[0].astype(int)) + " trovato nel BST!\n")
        bst_tree.delete(bst_tree.search(find_me))
        print(str(find_me[0].astype(int)), "eliminato dal BST!")
        print("- - - - - - - - - - ")
        bst_tree.print_inorder(bst_tree.get_root())
    else:
        print("\nValore " + str(find_me[0].astype(int)) + " non trovato nel BST!")

    print("\n# # # # # # # #")

    print("Red Black Tree:")
    rb_tree.print_tree()

    # Eliminazione valore nel RB
    rb_tree.delete_node(find_me)
    print("\n Eliminato " + str(find_me[0].astype(int)) + " dal RBTree!")
    rb_tree.print_tree()


if __name__ == "__main__":
    main()
