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

    def sum(self):
        sum = 0
        temp = self.head
        while temp:
            sum = sum + temp.data
            temp = temp.next
        print('sum = ', sum)

    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print('count', count)

ll = Linkedlist()
ll.begin(41)
ll.begin(22)
ll.begin(34)
ll.begin(41)
ll.sum()
ll.count()
ll.display()
