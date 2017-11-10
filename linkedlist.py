from node import Node


class LinkedList:
    def __init__(self):
        self.head = Node('head')

    def append(self, data):
        next_ = self.head
        while next_.next is not None:
            next_ = next_.next
        e = Node(data)
        next_.next = e

    def __repr__(self):
        string = ''
        next_ = self.head
        while next_ is not None:
            string += '{} > '.format(next_)
            next_ = next_.next
        return string

    def reverse(self):
        head = self.head.next
        lt = []
        while head is not None:
            lt.append(head.element)
            head = head.next
        lt = lt[::-1]

        self.head.next = None
        for e in lt:
            self.append(e)
        return self.head


def test():
    l = LinkedList()
    l.head = Node('head')
    l.append(111)
    l.append(222)
    l.append(333)
    l.reverse()
    assert str(l) == 'head > 333 > 222 > 111 > '


if __name__ == '__main__':
    test()