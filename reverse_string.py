def reverse_string(s):
    length = len(s) - 1
    string = ''
    for i in range(length, -1, -1):
        string += s[i]
    return string

def test():
    s = 'hello,world'
    assert reverse_string(s) == s[::-1]

if __name__ == '__main__':
    test()