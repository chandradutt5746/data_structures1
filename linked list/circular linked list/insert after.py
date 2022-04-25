class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.last = None

    def insert_empty(self, data):
        if self.last != None:
            return self.last

        newnode = Node(data)
        self.last = newnode
        self.last.next = self.last

    def insert_begin(self, data):
        if self.last == None:
            return self.insert_empty(data)
        newnode = Node(data)
        newnode.next = self.last.next
        self.last.next = newnode
        return self.last

    def insert_end(self, data):
        if self.last == None:
            return self.insert_empty(data)
        newnode = Node(data)
        newnode.next = self.last.next
        self.last.next = newnode
        self.last = newnode
        return self.last

    def insert_after(self, data, pos):
        if self.last == None:
            return self.insert_empty(data)
        newnode = Node(data)
        temp = self.last.next
        while temp:
            if temp.data == pos:
                newnode.next = temp.next
                temp.next = newnode

                if temp.data == self.last:
                    self.last = newnode
                    return self.last
                else:
                    return self.last
            temp = temp.next
            if temp.next == self.last:
                return 'no node found'

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
cl.insert_end(2)
cl.insert_end(3)
cl.insert_end(4)
cl.insert_end(5)
cl.insert_end(6)
print(cl.insert_after(100, 4))
cl.display()
