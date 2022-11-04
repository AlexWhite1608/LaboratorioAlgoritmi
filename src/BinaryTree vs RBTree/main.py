from BinarySearchTree import *
import numpy as np


def main():
    tree = BinarySearchTree()

    values = np.random.randint(1, 101, 10)

    for v in values:
        tree.add_node(tree.get_root(), v)

    tree.print_inorder(tree.get_root())


if __name__ == "__main__":
    main()
