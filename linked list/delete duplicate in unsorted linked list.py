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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_common(self):
        # if not self.head:
        #     return self.head
        # mset = set()
        # curr = self.head
        # prev = Node(None)
        # while curr:
        #     val = curr.data
        #     if val in mset:
        #         prev.next = curr.next
        #     else:
        #         mset.add(val)
        #         prev = curr
        #     curr = curr.next
        # return self.head

        if not self.head:
            return self.head

        mset = set()
        curr = self.head
        prev = None
        while curr:
            if curr.data in mset:
                prev.next = curr.next
            else:
                mset.add(curr.data)
                prev = curr
            curr = curr.next
        return self.head

        # curr = self.head
        # temp = curr.next
        # while curr:
        #     # if curr.data is temp.data:
        #     temp = curr.next
        #     while temp:
        #         if curr.data == temp.data:
        #             temp = temp.next
        #             curr.next = temp
        #         else:
        #             temp = temp.next
        #     curr = curr.next


ll = LinkedList()
ll.begin(5)
ll.begin(4)
ll.begin(3)
ll.begin(3)
ll.begin(2)
ll.begin(1)
ll.begin(1)
ll.delete_common()
ll.display()
