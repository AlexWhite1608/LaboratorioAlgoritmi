from Node import *


class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        # se non si fornisce il nodo allora si inserisce nella radice direttamente
        if node is None:
            self.root = Node(value)
        else:
            # inserimento nel figlio sinistro
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.addNode(node.left, value)

            else:
                if (node.right is None):
                    node.right = Node(value)
                else:
                    self.addNode(node.right, value)

    def printInorder(self, node):
        if node is not None:
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)
