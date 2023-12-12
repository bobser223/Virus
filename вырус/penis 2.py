def str_to_int(s, begin, end):
    val = 0
    negative = False

    if s[begin] == '+':
        begin += 1
    elif s[begin] == '-':
        negative = True
        begin += 1

    for i in range(begin, end):
        val *= 10
        val += ord(s[i]) - ord('0')

    if val == 0 and s[begin] != '0':
        val += 1

    if negative:
        val *= -1

    return val


def int_to_str(val):
    s = ""
    tmp = ""

    if val > 0:
        s += '+'
    else:
        val *= -1
        s += '-'

    while val > 0:
        tmp += chr(val % 10 + ord('0'))
        val //= 10

    for i in range(len(tmp) - 1, -1, -1):
        s += tmp[i]

    return s


def erase_the_plus(s):
    if s[0] == '+':
        s = s[1:]
    return s


def erase_the_one(s):
    if s[1] == '1' and len(s) == 2:
        s = s[:1]
    return s


def analyze(s, v):
    if 'x' not in s:
        v[0] += str_to_int(s, 0, len(s))
    else:
        if '^' not in s:
            v[1] += str_to_int(s, 0, s.find('x'))
        else:
            power = str_to_int(s, s.find('^') + 1, len(s))
            v[power] += str_to_int(s, 0, s.find('x'))


def decompose(s):
    v = [0] * 11
    i = 0

    while i < len(s):
        cur_s = s[i]
        i += 1

        while i < len(s) and s[i] not in ['+', '-']:
            cur_s += s[i]
            i += 1

        analyze(cur_s, v)

    return v


def multiplicate(a, b):
    c = [0] * 21

    for i in range(len(c)):
        c[i] = 0

    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]

    return c


def compose(v):
    s = ""

    for i in range(len(v) - 1, 1, -1):
        if v[i] != 0:
            coef = int_to_str(v[i])
            coef = erase_the_one(coef)
            s += coef + 'x^' + str(i)

    if v[1] != 0:
        coef = int_to_str(v[1])
        coef = erase_the_one(coef)
        s += coef + 'x'

    if v[0] != 0:
        s += int_to_str(v[0])

    return s


def main():
    a = input().strip()
    b = input().strip()

    a_decomposed = decompose(a)
    b_decomposed = decompose(b)

    c_decomposed = multiplicate(a_decomposed, b_decomposed)

    c = compose(c_decomposed)
    c = erase_the_plus(c)

    if len(c) > 0:
        print(c)
    else:
        print(0)


if __name__ == "__main__":
    main()






