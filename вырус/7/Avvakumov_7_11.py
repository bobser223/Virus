def vkatu(n, k):
    p = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p1 = ''
    while n > 0:
        p1 = p[n % k] + p1
        n //= k
    return p1

def pal(a):
    a = str(a)
    if a == a[::-1]:
        return True

p = []
counter = 0
n = int(input())
for i in range(2, 37):
    m = vkatu(n, i)
    if pal(m):
        p.append(i)
        counter += 1
if counter == 0:
    print("none")
elif counter == 1:
    print("unique")
    print(*p)
elif counter > 1:
    print("multiple")
    print(*p)
