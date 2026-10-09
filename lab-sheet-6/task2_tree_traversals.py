
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

def inorder(n):
    if n:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)

def preorder(n):
    if n:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)

def postorder(n):
    if n:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")

def iterative_inorder(n):
    stack = []
    while stack or n:
        while n:
            stack.append(n)
            n = n.left
        n = stack.pop()
        print(n.data, end=" ")
        n = n.right

def iterative_preorder(n):
    if not n:
        return
    stack = [n]
    while stack:
        n = stack.pop()
        print(n.data, end=" ")
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)

def iterative_postorder(n):
    if not n:
        return
    s1, s2 = [n], []
    while s1:
        n = s1.pop()
        s2.append(n)
        if n.left:
            s1.append(n.left)
        if n.right:
            s1.append(n.right)
    while s2:
        print(s2.pop().data, end=" ")

print("Recursive Inorder:")
inorder(root)
print("\nRecursive Preorder:")
preorder(root)
print("\nRecursive Postorder:")
postorder(root)

print("\nIterative Inorder:")
iterative_inorder(root)
print("\nIterative Preorder:")
iterative_preorder(root)
print("\nIterative Postorder:")
iterative_postorder(root)
print()
