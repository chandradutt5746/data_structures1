class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, root1, root2):
        if root1 is None:
           return []

        self.inorder(self.left)
        print(root1.data)
        self.inorder(self.right)

    def checktrees(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        return root1.data == root2.data and self.checktrees(root1.left, root2.left) and self.checktrees(root1.right, root2.right)


if __name__ == '__main__':
    root1 = Node(18)
    root1.left = Node(11)
    root1.left.left = Node(7)
    root1.left.left.left = Node(80)
    root1.right = Node(9)
    root1.right.left = Node(15)
    root1.right.right = Node(8)

    t = Node(root1)
    t.inorder(root1)

    root2 = Node(18)
    root2.left = Node(11)
    root2.left.left = Node(7)
    root2.left.left.left = Node(80)
    root2.right = Node(9)
    root2.right.left = Node(15)
    root2.right.right = Node(8)

    t = Node(root2)
    t.inorder(root2)


