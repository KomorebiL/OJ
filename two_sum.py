def two_sum(numbers, target):
    """
    给定一个数组，找到和为目标数字的一对数字。返回它们的下标。
    """
    dt = {}
    for i, n in enumerate(numbers):
        dt[n] = i

    for i, n in enumerate(numbers):
        _n = target - n
        value = dt.get(_n, False)
        if value is not False:
            return i, value
    return False


def test():
    numbers = [2, 7, 11, 15]
    target = 9
    assert set(two_sum(numbers, target)) == {0, 1}


if __name__ == '__main__':
    test()