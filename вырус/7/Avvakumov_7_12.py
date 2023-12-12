def binn(a):
    i = 0
    while a > 0:
        i += a % 2
        a //= 2
    return i


n, m = [i for i in input().split()]
p = 0
for el in range(int(n), int(m) + 1):
    p += binn(el)

print(p)