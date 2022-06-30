def infixtopostfix(exp):
    """a+b*(c^d-e)^(f+g*h)-i"""
    stack = []
    result = ''
    precedence = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4}

    for char in exp:
        if char in precedence.keys() or char == ')':
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == '(':
                    stack.append(char)
                elif char == '^' and stack[-1] == '^':
                    stack.append(char)
                elif char == ')':
                    outchar = stack.pop()
                    while outchar != '(':
                        result += outchar
                        outchar = stack.pop()
                elif precedence.get(char) == precedence.get(stack[-1]):
                    result += stack.pop()
                    stack.append(char)
                elif precedence.get(char) > precedence.get(stack[-1]):
                    stack.append(char)
                elif precedence.get(char) < precedence.get(stack[-1]):
                    while precedence.get(stack[-1]) >= precedence.get(char):
                        outchar = stack.pop()
                        result += outchar
                        if len(stack) == 0:
                            break
                    stack.append(char)
        else:
            result += char
    while len(stack) != 0:
        result += stack.pop()
    return result


exp = "a+b*(c^d-e)^(f+g*h)-i"
print(infixtopostfix(exp))
