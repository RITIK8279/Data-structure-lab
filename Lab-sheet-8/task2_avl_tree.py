
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def rotate_right(y):
    x = y.left
    t = x.right
    x.right = y
    y.left = t
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    root.height = 1 + max(height(root.left), height(root.right))
    balance = height(root.left) - height(root.right)
    if balance > 1 and key < root.left.data:
        return rotate_right(root)
    return root

root = None
for x in [30, 20, 10]:
    root = insert(root, x)

print("AVL root:", root.data)
