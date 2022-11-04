from BinarySearchTree import *
import numpy as np


def main():
    tree = BinarySearchTree()

    values = np.random.randint(1, 10, 5)

    for v in values:
        tree.add_node(tree.get_root(), v)

    tree.print_inorder(tree.get_root())

    find_me = np.random.randint(1, 10, 1)

    if tree.search(tree.get_root(), find_me) is True:
        print("Valore " + str(find_me[0].astype(int)) + " trovato!")
    else:
        print("Valore " + str(find_me[0].astype(int)) + " non trovato!")


if __name__ == "__main__":
    main()
