a,k = [int(d) for d in input().split()]
m = [int(d) for d in input().split()]
r=0
p=m
m=tuple(m)
for i in range(a):
    if m[i]==1:
        o=m[i]
        p.pop(i)
        r=i
p[0]=o
if r!=0:
    for i in range(1,r):
        p[i + 1] = m[i]

print(p)

print(p[k-1])
