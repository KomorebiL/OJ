from node import Node


class Stack():
    def __init__(self):
        self.head = Node('head')

    def empty(self):
        return self.head.next is None

    def push(self, element):
        self.head.next = Node(element, self.head.next)

    def pop(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node.element

    def top(self):
        return self.head.next

    def __repr__(self):
        next_ = self.head
        s = ''
        while next_ is not None:
            s += '{} > '.format(next_)
            next_ = next_.next
        return s


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    assert str(s) == 'head > 4 > 3 > 2 > 1 > '
    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1

if __name__ == '__main__':
    test_stack()