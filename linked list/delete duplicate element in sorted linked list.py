class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def duplicate(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = new
            else:
                temp = temp.next


ll = Linkedlist()
ll.begin(3)
ll.begin(3)
ll.begin(2)
ll.begin(2)
ll.begin(1)
ll.begin(1)
ll.display()
ll.duplicate()
print('after')
ll.display()
