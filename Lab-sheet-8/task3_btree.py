
class BTree:
    def __init__(self):
        self.keys = []

    def insert(self, key):
        self.keys.append(key)
        self.keys.sort()

tree = BTree()
for x in [10, 20, 5, 6, 12]:
    tree.insert(x)

print("B-Tree keys:", tree.keys)
