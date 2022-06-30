def validparanthesis(str):
    stack = []
    closetoopen = {'}': '{', ')': '(', ']': '['}

    for c in str:
        if c in closetoopen:
            if stack and stack[-1] == closetoopen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


str = '{}[]()'
print(validparanthesis(str))
