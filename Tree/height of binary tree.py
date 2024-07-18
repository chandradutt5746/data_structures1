class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, root, data):
        if not root:
            root = Node(data)
            return

        q = []
        q.append(root)

        while len(q):
            temp = q[0]
            q.pop(0)

            if not temp.left:
                temp.left = Node(data)
                break
            else:
                q.append(temp.left)

            if not temp.right:
                temp.right = Node(data)
                break
            else:
                q.append(temp.right)

    def inorder(self, root):
        if not root:
            return []
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


if __name__ == '__main__':
    root = Node(18)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.left.left = Node(80)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    t = Node(root)
    t.inorder(root)

    print('Height of tree', t.height(root))
