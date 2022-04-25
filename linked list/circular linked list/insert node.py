class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.last = None

    def insert_at_empty(self, data):
        if self.last != None:
            return self.last

        newnode = Node(data)
        self.last = newnode
        self.last.next = self.last

    def insert_begin(self, data):
        if self.last == None:
            return self.insert_at_empty(data)

        newnode = Node(data)
        newnode.next = self.last.next
        self.last.next = newnode
        return self.last

    def insert_end(self, data):
        if self.last == None:
            return self.insert_at_empty(data)

        newnode = Node(data)
        newnode.next = self.last.next
        self.last.next = newnode
        self.last = newnode
        return self.last

    def display(self):
        if self.last == None:
            return 'list is empty'

        temp = self.last.next
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.last.next:
                break


cl = CircularList()
cl.insert_begin(1)
cl.insert_begin(4)
cl.insert_begin(5)
cl.insert_begin(6)
cl.insert_end(44)
cl.insert_end(3)
cl.display()
