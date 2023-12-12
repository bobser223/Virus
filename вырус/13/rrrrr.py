def g(file):
    f = open(file)
    p = []

    while True:
        a = f.readline().strip()
        if len(a) == 0:
            break

        words = a.split()
        kilprop = (len(words) - 1) * 2
        leng = len(a)
        curprop = (80 - leng + kilprop) // max((len(words) - 1), 1)
        ost = (80 - leng + kilprop) % max((len(words) - 1), 1)
        a2 = words[0]

        for i in range(1, len(words)):
            kprop = curprop + (1 if i <= ost else 0)
            a2 += ' ' * kprop + words[i]

        p.append(a2)

    f.close()

    f2 = open("H", "wt")
    for el in p:
        print(el, file=f2)
        print(len(el), file=f2)

    f2.close()
    return p


result = g("file_13_7")
print(result)
