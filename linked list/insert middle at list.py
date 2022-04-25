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

    def middle(self):
        slow = self.head
        fast = self.head
        while fast:
            fast = fast.next
            slow = slow.next
            fast = fast.next
        print('middle', slow.data)


ll = Linkedlist()
ll.begin(-111)
ll.begin(2)
ll.begin(3)
ll.begin(4)
ll.begin(500)
ll.display()
ll.middle()
