class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        newnode.prev = None

        if self.head is not None:
            self.head.prev = newnode

        self.head = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert_end(self, data):
        newnode = Node(data)
        temp = self.head

        if self.head is None:
            newnode.next = None
            self.head = newnode
            return self.head

        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.next = None
        newnode.prev = temp

    def insert_after(self, data, k):
        if k is None:
            return None
        temp = self.head
        while temp.next:
            if temp.data != k:
                temp = temp.next
        newnode = Node(data)
        nxt = temp.next
        newnode = temp.next
        temp.next = newnode
        newnode.prev = temp
        newnode.next = nxt
        nxt.prev = newnode
        if newnode.next:
            newnode.next.prev = newnode


dl = DoublyLinkedlist()
dl.insert_begin(1)
dl.insert_end(2)
dl.insert_end(3)
dl.insert_end(4)
dl.insert_end(5)
dl.insert_after(100, 3)
dl.display()