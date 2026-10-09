
def evaluate_postfix(exp):
    stack = []

    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        elif ch in '+-*/':
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a // b)

    return stack[-1]


exp = input("Enter postfix expression: ")
print("Result:", evaluate_postfix(exp))
