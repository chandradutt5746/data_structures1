class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def insert(self, temp, data):
        if not temp:
            root = temp.data
            return

        q = []
        q.append(temp)

        while len(q):
            temp = q[0]
            q.pop(0)

            if temp.left:
                temp.left = Node(data)
                break
            else:
                q.append(temp.left)

            if temp.right:
                temp.right = Node(data)
                break
            else:
                q.append(temp.right)

    def levelorder(self, root):
        b = []
        s = []
        s.append(root)

        while s:
            n = s.pop(0)
            b.append(n.data)

            if n.left:
                s.append(n.left)

            if n.right:
                s.append(n.right)

        return b


if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)


    print("Inorder traversal before insertion:", end=" ")
    tree.levelorder(root)

    data = 12
    tree.insert(root, data)

