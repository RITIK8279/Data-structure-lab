stack = []
size = 5

while True:
    print("\n1.Push  2.Pop  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        if len(stack) < size:
            x = int(input("Enter value: "))
            stack.append(x)
            print("Pushed:", x)
        else:
            print("Stack Overflow")

    elif ch == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack Underflow")

    elif ch == 3:
        print("Stack:", stack)

    elif ch == 4:
        break

    else:
        print("Invalid choice")
