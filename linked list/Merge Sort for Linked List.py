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
        while temp:
            print(temp.data)
            temp = temp.next

    def sortlist(self):
        if not self.head or not self.head.next:
            return self.head
        left = self.head
        right = self.getmid(self.head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortlist(left)
        right = self.sortlist(right)
        return self.merge(left, right)

    def getmid(self, head):
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, list1, list2):
        tail = dummy = Node(None)
        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

    """
    '''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def sortedMerge(self, head1, head2):
        # code here
        if head1 is None:
            return head2 # if head2 is None, then it returns an empty list
        elif head2 is None:
            return head1
        else:
            curr1 = head1
            curr2 = head2
           
            if curr1.data <= curr2.data:
                head = curr1
                curr = curr1
                curr1 = curr1.next
            else:
                head = curr2
                curr = curr2
                curr2 = curr2.next
            prev = curr
   
            while curr1 is not None and curr2 is not None:
                if curr1.data <= curr2.data:
                    curr = curr1
                    curr1 = curr1.next
                else:
                    curr = curr2
                    curr2 = curr2.next
                prev.next = curr
                prev = curr
               
            curr.next = curr2 if curr1 is None else curr1
           
            return head
           
   # Function to split a linked list into 2 halves        
    def frontBackSplit(self, head):
        front = back = temp = head
       
        if head is None or head.next is None:
            return head, None
       
        while temp.next is not None and temp.next.next is not None:
            back = back.next
            temp = temp.next.next
           
        middle = back
        back = back.next
        middle.next = None
       
        return [front, back]
   
   #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
           
        [front_head, back_head] = self.frontBackSplit(head)
       
        front_head = self.mergeSort(front_head)
        back_head = self.mergeSort(back_head)
       
        new_head = self.sortedMerge(front_head,back_head)
       
        return new_head
    
    """


ll = Linkedlist()
ll.begin(1)
ll.end(6)
ll.end(5)
ll.end(4)
ll.end(2)
ll.end(3)
ll.sortlist()
ll.display()
