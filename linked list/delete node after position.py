class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def delete(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.begin(5)
    ll.begin(4)
    ll.begin(3)
    ll.begin(2)
    ll.begin(1)
    ll.delete(1)
    ll.display()
