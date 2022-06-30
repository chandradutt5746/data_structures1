# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
#
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)
"""
implement stack using qequeue module

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

stack.pop()
stack.pop()
stack.pop()
print(type(stack))
"""

# implement stack using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None


    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode


    def pop(self):
        if self.head is None:
            return 'stack is empty'

        temp = self.head.next
        self.head.next = temp
        temp = self.head
        return 'deleted element' + temp.data
        del temp

    def peekelement(self):
        if self.head is None:
            raise Exception('stack is empty')
        print(self.head.data)


s = stack()
s.push(5)
s.push(4)
s.push(3)
# s.push(2)
# s.push(1)
s.peekelement()