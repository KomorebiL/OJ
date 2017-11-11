from stack import Stack


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def empty(self):
        return self.s2.empty()

    def enqueue(self, element):
        if self.empty():
            self.s2.push(element)
        else:
            while not self.s2.empty():
                self.s1.push(self.s2.pop())
            self.s2.push(element)
            while not self.s1.empty():
                self.s2.push(self.s1.pop())

    def dequeue(self):
        return self.s2.pop()

    def __repr__(self):
        return str(self.s2)


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