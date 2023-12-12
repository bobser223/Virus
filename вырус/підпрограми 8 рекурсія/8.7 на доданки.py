# def comb(a, d: list):
#     if a == 1:
#         d.append(a)
#         print(*d)
#     else:
#         for i in range(1, a):
#             d1 = d[:]
#             d1.append(i)
#             comb(a-i, d1)
# comb (3, [])
# print(comb(3, 0))


def comb(a, p, lst: list):
    if a == 1:
        print(*lst)
    else:
        for i in range(p, a + 1):
            d1 = lst[:]
            d1.insert(0, i)
            comb(a-i,i, d1)
# comb (3, [])
print(comb(4, 1, []))