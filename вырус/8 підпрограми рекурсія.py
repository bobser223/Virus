p = 1
q = 1
pust = []
while p >= 0 and q >= 0:
    p, q = [int(i) for i in input().split()]
    if p < 0 and q < 0:
        break
    pust.append(p)
    pust.append(q)
print(pust)
c = 0
for i in range(0,len(pust),2):
    print(i)
    print(i+1)
    for i1 in range(pust[i], pust[i+1]):
        print(i1)



