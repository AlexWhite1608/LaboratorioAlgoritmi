class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.data = value

        if parent is None:
            self.parent = self
        else:
            self.parent = parent


class RBNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.color = 1  # 1 --> Red
