class Tree(object):
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def traversal(self):
        # 前序遍历
        print(self.element)
        if self.left is not None:
            self.left.traversal()
        if self.right is not None:
            self.right.traversal()

    @classmethod
    def reversal(cls, tree):
        tree.left, tree.right = tree.right, tree.left
        if tree.left is not None:
            cls.reversal(tree.left)
        if tree.right is not None:
            cls.reversal(tree.right)


def test():
    a = Tree(0)
    b = Tree(1)
    c = Tree(2)
    d = Tree(3)
    e = Tree(4)
    f = Tree(5)
    g = Tree(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    a.traversal()
    print('---------------------------')
    Tree.reversal(a)
    a.traversal()


if __name__ == '__main__':
    test()