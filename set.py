class Set:
    def __init__(self, *args):
        self.data = []
        for s in args:
            self.add(s)

    def remove(self, x):
        for i, s in enumerate(self.data):
            if s is x:
                self.data = self.data[0: i] + self.data[i + 1:]

    def add(self, x):
        bool_ = self.has(x)
        if bool_ is False:
            self.data.append(x)

    def has(self, x):
        for s in self.data:
            if s is x:
                return True
        return False

    def __repr__(self):
        string = '{'
        for s in self.data:
            string += '{}, '.format(str(s))
        string = string[:-2] + '}'
        return string


def test():
    set_ = Set(1, 2, 2, 3, 3, 4)
    assert str(set_) == '{1, 2, 3, 4}'
    set_.remove(2)
    assert str(set_) == '{1, 3, 4}'


if __name__ == '__main__':
    test()