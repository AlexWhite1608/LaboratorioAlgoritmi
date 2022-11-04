class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add_node(self, node, value):
        if node is None:
            self.root = Node(value)
        else:
            if value < node.data:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.add_node(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self.add_node(node.right, value)

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.data)
            self.print_inorder(node.right)
