class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

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

    def add_nodes(self, first, second):
        s1 = ""
        s2 = ""
        temp1 = first
        temp2 = second

        while temp1:
            s1 += str(temp1.data)
            temp1 = temp1.next
        while temp2:
            s2 += str(temp2.data)
            temp2 = temp2.next

        v = str(int(s1) + int(s2))
        ll1 = Node()
        for i in v:
            ll1.insert(i)
        return ll1.head

        # dummy = Node(0)
        # cur = dummy
        #
        # carry = 0
        # while l1 or l2 or carry:
        #     v1 = l1.data if l1 else 0
        #     v2 = l2.data if l2 else 0
        #
        #     val = v1 + v2 + carry
        #     carry = val // 10
        #     val = val % 10
        #     cur.next = Node(val)
        #
        #     cur = cur.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        #
        # return dummy.next


l1 = Linkedlist()
l1.begin(1)
l1.end(2)
l1.end(3)
print('list 1')
l1.display()


l2 = Linkedlist()
l2.begin(6)
l2.end(9)
l2.end(8)
print('list 2')
l2.display()

ll = Linkedlist()
l1.add_nodes(l1, l2)
