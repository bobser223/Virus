#def g():
def g(file):
    f = open(file)
    p = []
    while True:
        a = f.readline()
        if len(a) == 0:
            break
        words = a.split()
        if len(a) == 1:
            p.append(a)
        leng = len(a)
        curprop = (80 - len(''.join(words))) // (len(words) - 1)
        ost = (80 - len(''.join(words))) % (len(words) - 1)
        a2 = words[0]
        for i in range(1, len(words)):
            kprop = curprop + (1 if i <= ost else 0)
            a2 += ' ' * kprop + words[i]
        p.append(a2)
    f.close()
    # return p
    f2 = open("H", "wt")
    for el in p:
        print(el, file=f2)
        print(len(el), file=f2)
    f2.close()
g("file_13_7")

# def g(file):
#     f = open(file)
#     p = []
#     while True:
#         a = f.readline()
#         if len(a) == 0:
#             break
#         words = a.split()
#         if len(a) == 1:
#             p.append(a)
#         leng = len(a)
#         curprop = (80 - len(a)) // (len(words) - 1)
#         ost = (80 - len(a)) % (len(words) - 1)
#         a2 = words[0]
#         for i in range(1, len(words)):
#             kprop = curprop + (1 if i <= ost else 0)
#             a2 += ' ' * kprop + words[i]
#         p.append(a2)
#     f.close()
#     # return p
#     f2 = open("H", "wt")
#     for el in p:
#         print(el, file=f2)
#         print(len(el), file=f2)
#     f2.close()
# print(g("file_13_7"))