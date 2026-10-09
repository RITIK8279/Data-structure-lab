class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, x):
        n = Node(x)

        if self.rear is None:
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        print("Deleted:", self.front.data)
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        t = self.front
        while t:
            print(t.data, end=" ")
            t = t.next
        print()

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

q.dequeue()

print("After Dequeue:")
q.display()
