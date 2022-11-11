class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.data = value

        if parent is None:
            self.p = self
        else:
            self.p = parent