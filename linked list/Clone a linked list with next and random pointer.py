class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def getlist(self):
        OldtoCopy = {None : None}
        temp = self.head
        while temp:
            copy = Node(temp.data)
            OldtoCopy[temp] = copy
            temp = temp.next

        temp = self.head
        while temp:
            copy = OldtoCopy[temp]
            copy.next = OldtoCopy[temp.next]
            copy.random = OldtoCopy[temp.random]
            temp = temp.next
        return OldtoCopy[self.head]
