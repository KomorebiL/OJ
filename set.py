class Set:
    def __init__(self, *args):
        self.set = []
        for s in args:
            self.add(s)

    def remove(self, x):
        for i, s in enumerate(self.set):
            if s is x:
                self.set = self.set[0: i] + self.set[i + 1:]

    def add(self, x):
        bool_ = self.has(x)
        if bool_ is False:
            self.set.append(x)

    def has(self, x):
        for s in self.set:
            if s is x:
                return True
        return False

    def __repr__(self):
        string = '{'
        for s in self.set:
            string += '{}, '.format(str(s))
        string = string[:-2] + '}'
        return string

    def __eq__(self, other):
        if len(other.set) == len(self.set):
            for s in other.set:
                bool_ = self.has(s)
                if bool_ is False:
                    return False
            return True
        else:
            return False

    def __contains__(self, x):
        return self.has(x)


def test():
    a = Set(1, 2, 2, 3, 4, 4)
    b = Set(1, 2, 2, 3, 4)
    c = Set(1, 3, 4, 2)
    d = Set(2, 3)
    assert (str(a) == '{1, 2, 3, 4}')
    print(a, b, c, d)
    assert (a == b)
    assert (a == c)
    assert (a != d)
    assert (1 in a)
    assert (a.has(1) is True)
    a.remove(1)
    assert (a.has(1) is False)
    a.add(1)
    assert (a.has(1) is True)


if __name__ == '__main__':
    test()