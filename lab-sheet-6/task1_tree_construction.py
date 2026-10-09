
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Binary Tree Created Successfully")
print("Root:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)
