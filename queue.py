from node import Node


class Queue:
    def __init__(self):
        self.head = Node('head')
        self.tail = self.head

    def empty(self):
        return self.head == self.tail

    def enqueue(self, element):
        n = Node(element)
        self.tail.next = n
        self.tail = n

    def dequeue(self):
        if self.head.next == self.tail:
            node = self.tail
            self.tail = self.head
            self.head.next = None
            return node.element
        else:
            node = self.head.next
            self.head.next = node.next
            return node.element

    def __repr__(self):
        next_ = self.head
        s = ''
        while next_ is not None:
            s += '{} > '.format(next_)
            next_ = next_.next
        return s


def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert str(q) == 'head > 1 > 2 > 3 > 4 > '
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4


if __name__ == '__main__':
    test_queue()