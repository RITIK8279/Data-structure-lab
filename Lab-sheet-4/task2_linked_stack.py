class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        n = Node(x)
        n.next = self.top
        self.top = n

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Popped:", self.top.data)
            self.top = self.top.next

    def display(self):
        t = self.top
        while t:
            print(t.data, end=" ")
            t = t.next
        print()

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack:")
s.display()

s.pop()

print("After Pop:")
s.display()
