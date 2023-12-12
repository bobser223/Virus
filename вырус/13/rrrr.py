def g(file):
    f = open(file)
    p = []

    while True:
        a = f.readline()
        if len(a) == 0:
            break

        words = a.split()

        if len(words) == 1:
            p.append(a.strip())  # Используем strip() для удаления лишних пробелов и символов новой строки

        curprop = (80 - len(a)) // (max(len(words) - 1, 1))
        ost = (80 - len(a)) % max((len(words) - 1), 1)
        a2 = words[0]

        for i in range(1, len(words)):
            kprop = curprop + (1 if i <= ost else 0)
            a2 += ' ' * kprop + words[i]

        p.append(a2.strip())  # Используем strip() для удаления лишних пробелов и символов новой строки

    f.close()

    f2 = open("H", "wt")
    for el in p:
        print(el, file=f2)
        print(len(el), file=f2)
    f2.close()

g("file_13_7")
