class UnionFind:
    def __init__(self, size):
        self.parent = []
        self.weight = []

        for node in range(size):
            self.parent.append(node)
            self.weight.append(0)

    def find(self, node):
        if self.parent[node] == node:
            return node
        else:
            return self.find(self.parent[node])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.weight[x_root] < self.weight[y_root]:
            self.parent[x_root] = x_root
        elif self.weight[x_root] > self.weight[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.weight[x_root] += 1
