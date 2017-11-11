class HashTable:
    def __init__(self):
        self.table_size = 10007
        self.table = [None] * self.table_size

    def get(self, key, value=None):
        if self._has(key) is True:
            return self._return_value(key)
        else:
            return value

    def set(self, key, value):
        index = self._index(key)
        data = (key, value)
        if self.table[index] is None:
            self.table[index] = [data]
        else:
            lt = self.table[index]
            _bool = False
            for i, s in enumerate(lt):
                if s[0] is key:
                    lt[i] = data

            if _bool is False:
                lt.append(data)

    def _return_value(self, key):
        index = self._index(key)
        lt = self.table[index]
        for data in lt:
            if data[0] == key:
                return data[1]

    def _has(self, key):
        index = self._index(key)
        lt = self.table[index]
        if lt is not None:
            for data in lt:
                if data[0] == key:
                    return True
        return False

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
        return self._hash(key) % self.table_size

    def __contains__(self, key):
        return self._has(key)


def test_heshtable():
    names = [
        'komorebi',
        'mie',
        'lukey',
        'asd',
    ]
    t = HashTable()
    for i, k in enumerate(names):
        t.set(k, i)
    for i, k in enumerate(names):
        v = t.get(k)
        assert v == i
    assert ('komorebi' in t) is True
    assert ('lzsb' in t) is False

if __name__ == '__main__':
    test_heshtable()