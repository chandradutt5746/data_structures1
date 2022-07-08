class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(temp):
    if not temp:
        return []

    inorder(temp.left)
    print(temp.data)
    inorder(temp.right)


def preorder(temp):
    if not temp:
        return[]
    print(temp.data)
    preorder(temp.left)
    preorder(temp.right)


def postorder(temp):
    if not temp:
        return []
    postorder(temp.left)
    postorder(temp.right)
    print(temp.data)


def insert(temp, data):
    if not temp:
        root = Tree(data)
        return
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Tree(data)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Tree(data)
            break
        else:
            q.append(temp.right)


def levelorder(temp):
    b = []
    s = []
    s.append(temp)

    while s:
        n = s.pop(0)
        b.append(n.data)

        if n.left:
            s.append(n.left)

        if n.right:
            s.append(n.right)

    return b


if __name__ == '__main__':
    root = Tree(10)
    root.left = Tree(11)
    root.left.left = Tree(7)
    root.right = Tree(9)
    root.right.left = Tree(15)
    root.right.right = Tree(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)

    print()
    print('preorder traversal', end=' ')
    preorder(root)

    print()
    print('postorder traversal', end=' ')
    postorder(root)


    print()
    print('level order traversal', end='')
    levelorder(root)
