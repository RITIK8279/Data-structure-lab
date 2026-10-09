queue = []
size = 5

while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        if len(queue) < size:
            x = int(input("Enter value: "))
            queue.append(x)
            print("Inserted:", x)
        else:
            print("Queue Overflow")

    elif ch == 2:
        if queue:
            print("Deleted:", queue.pop(0))
        else:
            print("Queue Underflow")

    elif ch == 3:
        print("Queue:", queue)

    elif ch == 4:
        break

    else:
        print("Invalid choice")
