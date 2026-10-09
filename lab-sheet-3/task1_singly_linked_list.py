class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data, pos):
        new = Node(data)

        if pos == 0:
            new.next = self.head
            self.head = new
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new.next = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


s = SLL()
s.insert(10, 0)
s.insert(30, 1)
s.insert(20, 1)
print("Singly Linked List:")
s.display()

s.delete(20)
print("After deletion:")
s.display()
