def nsd(a,b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, (a % b)
    return a


def nskk(a_k):
    an = 1
    for i in range(2, a_k + 1):
        an = an * (i // nsd(i, an))
    return an

k = int(input())
print(nskk(k))

