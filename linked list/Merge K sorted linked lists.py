class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def mergeklist(self, arr, k):
        if not arr and len(arr) == 0:
            return None

        while len(arr) > 0:
            mergedlist = []
            for i in range(0, len(arr), 2):
                l1 = arr[i]
                l2 = arr[i+1]
                mergedlist.append(self.mergeklist(l1, l2))
            arr = mergedlist
        print(arr)
        return arr[0]


    def mergelist(self, l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1 > l2:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        print(dummy)
        return dummy.next

    def display(self):
        # if self.head == None:
        #     return None
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)

l2 = Node(4)
l2.next = Node(5)
Linkedlist.display(l1)
