from collections import deque


def get_min_pop(stack):
    stack.reverse()
    for ele in range(len(stack)-1):
        min = 99999999
        for ne in range(ele, len(stack)-1):
            if stack[ne] < stack[ele]:
                min = ne
            else:
                pass
            stack[ele] = min

    return stack


stack = deque()

stack.append(1)
stack.append(6)
stack.append(43)
stack.append(1)
stack.append(2)
stack.append(0)
stack.append(5)

# print(list(stack))
print(get_min_pop(stack))
