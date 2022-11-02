

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self.value:
            self.value = value
            return

        if self.value == value:
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = BinarySearchTree(value)
            return

        if self.right:
            self.right.insert(value)
            return
        self.right = BinarySearchTree(value)

    def min(self):
        temp = self
        while temp.left is not None:
            temp = temp.left
        return temp.value

    def max(self):
        temp = self
        while temp.left is not None:
            temp = temp.right
        return temp.value

    def search(self, value):
        if value == self.value:
            return True

        if value < self.value:
            if self.left == None:
                return False
            return self.left.search(value)

        if self.right == None:
            return False
        return self.right.exists(value)

    def preorder(self, values):
        if self.value is not None:
            values.append(self.value)
        if self.left is not None:
            self.left.preorder(values)
        if self.right is not None:
            self.right.preorder(values)
        return values

    def postorder(self, values):
        if self.left is not None:
            self.left.postorder(values)
        if self.right is not None:
            self.right.postorder(values)
        if self.value is not None:
            values.append(self.value)
        return values
