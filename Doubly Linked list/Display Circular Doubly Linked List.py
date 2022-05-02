class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylist:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        newnode = Node(data)
        newnode.next = self.head
        newnode.prev = newnode.next

        if self.head is not None:
            self.head.prev = newnode
        self.head = newnode

    def insert_end(self, data):
        newnode = Node(data)
        if self.head is None:
            newnode.next = self.head
            self.head = newnode
            self.head.next = self.head.prev
            self.head.prev = self.head.next
            return self.head
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.next = temp.prev
        newnode.prev = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.head.next:
                break

dl = Doublylist()
dl.insert_head(1)
dl.insert_head(2)
dl.insert_head(3)
dl.insert_end(20)
# dl.insert_end(3)
# dl.insert_end(4)
# dl.insert_end(5)
dl.display()
