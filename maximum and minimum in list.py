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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def max(self):
        max = 0
        temp = self.head
        while temp:
            if max < temp.data:
                max = temp.data
            temp = temp.next
        print('max = ', max)

    def min(self):
        min = 123
        temp = self.head
        while temp:
            if min > temp.data:
                min = temp.data
            temp = temp.next
        print('min = ', min)


ll = Linkedlist()
ll.begin(-111)
ll.begin(2)
ll.begin(3)
ll.begin(4)
ll.begin(500)
ll.max()
ll.min()
ll.display()
