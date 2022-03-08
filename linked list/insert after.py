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

    def insert_after(self, data):
        prevnode = int(input('enter node value after insert newnode: '))
        temp = self.head
        if temp is None:
            print('no node available')
            return

        while temp:
            if temp.data == prevnode.data:
                newnode = Node(data)
                newnode.next = prevnode.next
                prevnode.next = newnode

    def display(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.end(1)
    ll.end(2)
    ll.end(3)
    ll.end(4)
    ll.insert_after(5)
    ll.display()
