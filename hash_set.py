class HashSet:
    def __init__(self, *args):
        self.set_size = 10007
        self.set = [None] * self.set_size
        for s in args:
            self.add(s)

    def add(self, x):
        if self.has(x) is False:
            index = self._index(x)
            self.set[index] = x

    def remove(self, x):
        if self.has(x) is True:
            index = self._index(x)
            self.set = self.set[0: index] + self.set[index + 1:]

    def has(self, x):
        index = self._index(x)
        v = self.set[index]
        if v is x:
            return True
        else:
            return False

    @staticmethod
    def refine(_set):
        data = [s for s in _set if s is not None]
        return data

    @staticmethod
    def _hash(s):
        index = 0
        factor = 1
        for c in str(s):
            ascii_ = ord(c)
            index += ascii_ * factor
            factor *= 10
        return index

    def _index(self, key):
        return self._hash(key) % self.set_size

    def __repr__(self):
        data = self.refine(self.set)
        string = '{'
        for s in data:
            string += '{}, '.format(str(s))
        string = string[:-2] + '}'
        return str(string)

    def __eq__(self, other):
        other = self.refine(other.set)
        this = self.refine(self.set)
        if len(other) == len(this):
            for s in other:
                bool_ = self.has(s)
                if bool_ is False:
                    return False
            return True
        else:
            return False

    def __contains__(self, x):
        return self.has(x)

    def __len__(self):
        data = self.refine(self.set)
        return len(data)


def test():
    a = hash_set(1, 2, 2, 3, 4, 4)
    b = hash_set(1, 2, 2, 3, 4)
    c = hash_set(1, 3, 4, 2)
    d = hash_set(2, 3)
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