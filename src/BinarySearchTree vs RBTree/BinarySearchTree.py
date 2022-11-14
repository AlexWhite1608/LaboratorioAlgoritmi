import TreeNode as tn


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def minimum(self, node):
        x = None
        while node.left is not None:
            x = node.left
            node = node.left
        return x

    def maximum(self, node):
        x = None
        while node.right is not None:
            x = node.right
            node = node.right
        return x

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.data)
            self.print_inorder(node.right)

    # Ricerca il valore inserito e restituisce True/False
    def find(self, node, value):
        if node is None or value is None:
            return False

        elif node.data == value:
            return True

        elif node.data < value:
            return self.find(node.right, value)

        else:
            return self.find(node.left, value)

    def insert(self, value):
        t = tn.Node(value)
        parent = None
        node = self.root
        while node is not None:
            parent = node
            if node.data > t.data:
                node = node.left
            else:
                node = node.right
        t.parent = parent
        if parent is None:
            self.root = t
        elif t.data < parent.data:
            parent.left = t
        else:
            parent.right = t
        return t

    # Ritorna direttamente il nodo corrispondente al valore scelto
    def search(self, value):
        node = self.root
        while node is not None:
            if node.data == value:
                return node
            if node.data > value:
                node = node.left
            else:
                node = node.right
        return None

    def successor(self, node):
        parent = None
        if node.right is not None:
            return self.minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def predecessor(self, node):
        parent = None
        if node.left is not None:
            return self.maximum(node.left)
        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    def transplant(self, node, new_node):
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        if new_node is not None:
            new_node.parent = node.parent

    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.p != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.parent = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.parent = succ
