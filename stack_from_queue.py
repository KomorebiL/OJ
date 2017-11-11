from queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def empty(self):
        return self.q1.empty()

    def push(self, element):
        if self.empty():
            self.q1.enqueue(element)
        else:
            self.q2.enqueue(element)
            while not self.q1.empty():
                self.q2.enqueue(self.q1.dequeue())
            self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.dequeue()

    def top(self):
        return self.q1.head.next.element

    def __repr__(self):
        return str(self.q1)


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