
def infix_to_postfix(exp):
    stack = []
    result = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for ch in exp:
        if ch.isalnum():
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   (priority[stack[-1]] > priority[ch] or
                    (priority[stack[-1]] == priority[ch] and ch != '^'))):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


exp = input("Enter infix expression: ")
print("Postfix expression:", infix_to_postfix(exp))
