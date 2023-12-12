def vkatu(n, k):
    p = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p1 = ''
    while n > 0:
        p1 = p[n % k] + p1
        n //= k
    return p1


def vdes(a, m):
    if m == 10:
        return int(a)
    b = int(a, m)
    return b

m, k = [ int(i) for i in input().split()]
n = input()

print(vkatu(vdes(n, m), k))
