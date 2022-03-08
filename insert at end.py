class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def begin(self, data):
        newnode = Node(data)
        self.head = newnode
        newnode.next = None

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


if __name__ == '__main__':
    ll = LinkedList()
    ll.begin(1)
    ll.end(3)
    ll.display()
