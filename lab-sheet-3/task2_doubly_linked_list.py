class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new = Node(data)

        if self.head is None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def delete(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev
        else:
            self.tail = temp.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def reverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


d = DLL()
d.insert(10)
d.insert(20)
d.insert(30)

print("Doubly Linked List:")
d.display()

d.delete(20)
print("After deletion:")
d.display()

print("Reverse traversal:")
d.reverse()
