from BinaryTree import *


def main():
    tree = BinaryTree()

    for x in range(10):
        tree.addNode(None,x)
        tree.printInorder(tree.root)



if __name__ == "__main__":
    main()
