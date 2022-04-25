class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


class CircularList:
    def __init__(self):
        self.last = None

    def insert_empty(self, data):
        if self.last != None:
            return None
        newnode = Node(data)
        self.last = newnode
        self.last.next = self.last

    def begin(self, data):
        if self.last == None:
            return self.insert_empty(data)
        newnode = Node(data)
        newnode.next = self.last.next
        self.last.next = newnode
        return self.last

    def end(self, data):
        if self.last == None:
            return self.insert_empty(data)

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

    def delete_end(self):
        if self.last == None:
            return 'list is empty'

        temp = self.last.next
        while temp.next != self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp
        del temp


cl = CircularList()
cl.begin(1)
cl.end(2)
cl.end(3)
cl.end(3)
cl.end(4)
cl.end(5)
cl.end(5)
cl.delete_end()
cl.display()
