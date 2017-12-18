def encoding(string):
    last = 256
    d = {chr(i): i for i in range(last)}

    p = ''
    lt = []
    for s in string:
        ps = p + s
        if ps in d:
            p = ps
        else:
            lt.append(d[p])
            d[ps] = last
            last += 1
            p = s
    return lt


def decoding():
    pass


def main():
    string = 'asdasdasd'
    data = encoding(string)
    print(data)


if __name__ == '__main__':
    main()
