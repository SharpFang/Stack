def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(int(num1 / num2))

    return stack[0]

# Приклад
rpn_tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(rpn_tokens))  # Вивід: 9
