def suma(a):
    if a == 0:
        return 0
    if (a % 10) > 0:
        return a % 10
    else:
        return suma(a / 10)
# сумма функцій
p = 1
q = 1
pust = []
while p >= 0 and q >= 0:
    p, q = [int(i) for i in input().split()]
    if p < 0 and q < 0:
        break
    pust.append(p)
    pust.append(q)
c = 0
for i in range(0,len(pust),2):
    pust[i] = p
    pust[i + 1] = q
    for i1 in range(pust[i], pust[i + 1] + 1):
        c += suma(i1)
    print(c)









