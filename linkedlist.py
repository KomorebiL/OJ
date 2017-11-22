from node import Node


class LinkedList:
    def __init__(self):
        self.head = Node('head')

    def op(self, f):
        head = self.head.next
        lt = []
        while head is not None:
            lt.append(head.element)
            head = head.next
        lt = f(lt)

        self.head.next = None
        for e in lt:
            self.append(e)
        return self.head

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
        # 翻转
        n1 = Node('head')
        next_ = self.head.next
        while next_ is not None:
            temp = Node(next_.element)
            n1_next = n1.next
            n1.next = temp
            temp.next = n1_next
            next_ = next_.next
        self.head = n1

    def sort(self):
        # 排序
        def f(lt):
            lt.sort()
            return lt
        return self.op(f)

    @classmethod
    def merge(cls, l1, l2):
        # 合并
        l3 = LinkedList()
        l3.head = Node('head')
        l1_next = l1.head.next
        l2_next = l2.head.next
        while True:
            if l1_next.element < l2_next.element:
                l3.append(l1_next.element)
                l1_next = l1_next.next
            else:
                l3.append(l2_next.element)
                l2_next = l2_next.next

            if l2_next is None:
                l3_next = l3.head
                while l3_next.next is not None:
                    l3_next = l3_next.next
                l3_next.next = l1_next
                break
            elif l1_next is None:
                l3_next = l3.head
                while l3_next is not None:
                    l3_next = l3_next.next
                l3_next.next = l2_next
                break
        return l3


def test_reverse():
    l = LinkedList()
    l.append(111)
    l.append(222)
    l.append(333)
    l.reverse()
    print(l)
    assert str(l) == 'head > 333 > 222 > 111 > '


def test_soft():
    l = LinkedList()
    l.append(5)
    l.append(2)
    l.append(1)
    l.append(3)
    l.sort()
    assert str(l) == 'head > 1 > 2 > 3 > 5 > '


def test_merge():
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(6)
    l2 = LinkedList()
    l2.append(2)
    l2.append(4)
    l2.append(5)
    l2.append(6)
    l3 = l1.merge(l1, l2)
    print(l3)
    assert str(l3) == 'head > 1 > 2 > 2 > 3 > 4 > 5 > 6 > 6 > '


if __name__ == '__main__':
    test_reverse()
    test_soft()
    test_merge()