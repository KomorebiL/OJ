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

    if p != '':
        lt.append(d[p])

    return lt


def decoding(lt):
    last = 256
    d = {i: chr(i) for i in range(last)}

    string = ''
    p = lt.pop(0)
    string += d[p]

    for i in lt:
        if i in d:
            temp = d[i]
        string += temp
        d[last] = d[p] + temp[0]
        last += 1
        p = i
    return string


def main():
    string = 'asd_asd_asd_asd_asd_asd_asd_asd'
    e_data = encoding(string)
    d_data = decoding(e_data)
    print(e_data, d_data, string == d_data)


if __name__ == '__main__':
    main()
