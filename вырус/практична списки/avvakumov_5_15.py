n=int(input())
m = [int(d) for d in input().split()]
p=[]
mi = min(m)
ma = max(m)
for el in m:
    if el != mi and el != ma:
        p.append(el)
    elif el == mi:
        p.append(ma)
    elif el == ma:
        p.append(mi)
print(*p)

