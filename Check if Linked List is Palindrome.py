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
        if self.head is None:
            return self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def is_palindrome(self):
        # without array
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse middle half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check if palindrome
        left = self.head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True

        # with array
        # arr = []
        # temp = self.head
        # while temp:
        #     arr.append(temp.data)
        #     temp = temp.next
        #
        # l, r = 0, len(arr) - 1
        # while l <= r:
        #     if arr[l] != arr[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True


ll = Linkedlist()
ll.begin(1)
ll.end(2)
ll.end(3)
ll.end(2)
ll.end(2)
ll.end(1)
ll.display()
print(ll.is_palindrome())