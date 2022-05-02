class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
        self.prev = None


class DoublyList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        newnode.prev = None

        if self.head is not None:
            self.head.prev = newnode
        self.head = newnode

    def insert_end(self, data):
        newnode = Node(data)
        temp = self.head
        if self.head is None:
            newnode.next = self.head
            self.head = newnode
            return self.head

        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp
        newnode.next = None
        # return self.head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse_list(self):
        temp = self.head
        curr = None

        while temp is not None:
            curr = temp.prev
            temp.prev = temp.next
            temp.next = curr
            temp = temp.prev

        if curr is not None:
            self.head = curr.prev
        # return self.head


dl = DoublyList()
dl.insert_begin(1)
dl.insert_end(2)
dl.insert_end(3)
dl.insert_end(4)
dl.insert_end(5)
print('before')
dl.display()
print('after')
dl.reverse_list()
dl.display()
