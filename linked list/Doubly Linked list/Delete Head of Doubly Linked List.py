class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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

    def insert_after(self, data, p):
        newnode = Node(data)
        if self.head is None and p == 1:
            return None
        if self.head is None and p > 1:
            return self.head
        temp = self.head
        while temp:
            p -= 1
            temp = temp.next

        if temp.next is None:
            temp.next = newnode
            newnode.prev = temp
            newnode.next = None
            return self.head

        temp.next = newnode
        temp.next.prev = newnode
        newnode.prev = temp
        return self.head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_head(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        # del temp


dl = DoublyList()
dl.insert_begin(1)
dl.insert_end(2)
dl.insert_end(3)
dl.insert_end(4)
dl.insert_end(5)

# dl.insert_after(100, 2)
print('before')
dl.display()
print('after')
dl.delete_head()
dl.display()
