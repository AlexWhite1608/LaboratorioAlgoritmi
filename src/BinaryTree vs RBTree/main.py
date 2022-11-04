from BinarySearchTree import *
import numpy as np


def main():
    tree = BinarySearchTree()

    # values = np.random.randint(1, 101, 10)

    for v in range(15):
        tree.add_node(tree.get_root(), v)

    tree.print_inorder(tree.get_root())

    find_me = 12

    if tree.search(tree.get_root(), find_me) is not False:
        print("Valore " + str(find_me) + " trovato!")
    else:
        print("Valore " + str(find_me) + " non trovato!")


if __name__ == "__main__":
    main()
