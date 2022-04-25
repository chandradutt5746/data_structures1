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

    def end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.next = None

    def rotate_list(self, k):
        tail = self.head
        while tail.next:
            tail = tail.next

        for i in range(k):
            tail.next = self.head
            self.head = self.head.next
            tail = tail.next
            tail.next = None
        return self.head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = Linkedlist()
ll.begin(1)
ll.end(2)
ll.end(3)
ll.end(4)
ll.end(5)
ll.end(6)
ll.display()
ll.rotate_list(3)
ll.display()
