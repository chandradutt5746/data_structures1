class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.next = None

    def display(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def identical(self, l1, l2):
        l1 = self.head
        l2 = self.head

        if l1 == None or l2 == None:
            return False

        while l1!=None and l2!=None:
            if l1.data != l2.data:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1==None and l2==None


l1 = LinkedList()
l1.end(1)
l1.end(2)
l1.end(3)
l1.end(4)
l1.end(5)
l1.end(6)
l1.display()

l2 = LinkedList()
l2.end(1)
l2.end(2)
l2.end(3)
l2.end(4)
l2.end(5)
l2.end(6)
l2.display()
print(l1.identical(l1, l2))
