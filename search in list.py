class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode

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

    def search(self, k):
        temp = self.head
        while temp:
            if temp.data == k:
                print('found = ', k)
                return
            temp = temp.next
        print('not', k)


ll = Linkedlist()
ll.end(5)
ll.end(4)
ll.end(3)
ll.end(2)
ll.end(1)
ll.search(30)
ll.display()
