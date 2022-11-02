from BinarySearchTree import *
import numpy as np


def main():
    tree = BinarySearchTree()

    numbers = np.random.randint(1, 101, 10)
    for i in numbers:
        tree.insert(i)

    print("Preorder:")
    print(tree.preorder([]))
    print("--------")

    print("Postorder:")
    print(tree.postorder([]))
    print("--------")


if __name__ == "__main__":
    main()
