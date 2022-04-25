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

    def count_loop(self, slow):
        count = 1
        temp = slow
        while temp.next:
            count += 1
            if temp == slow:
                print(count)
                break
            temp = temp.next

    def remove_loop_in_linkedlist(self):
        temp = self.head
        s = set()
        while temp:
            if temp not in s:
                s.add(temp)
                if temp.next in s:
                    temp.next = None
                    return
            temp = temp.next

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # self.remove_loop_in_linkedlist(slow)
                return self.count_loop(slow)

                # print('loop found')
        print('not found')
        # mset = set()
        # temp = self.head
        # while temp:
        #     if temp not in mset:
        #         mset.add(temp)
        #         temp = temp.next
        #     else:
        #         print('loop deteched')
        #         break
        #     # temp = temp.next
        # print('not detected')


    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.begin(1)
ll.end(2)
ll.end(3)
ll.end(4)
ll.end(5)
ll.detect_loop()
ll.display()
