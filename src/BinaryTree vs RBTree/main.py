from BinarySearchTree import *


def main():
    tree = BinarySearchTree()

    tree.addNode(tree.root, 101)
    for x in range(100):
        tree.addNode(None, x)

    tree.printInorder(tree.root)


if __name__ == "__main__":
    main()
