n = int(input())
m = [float(d) for d in input().split()]
ma = max(m)
p = []
s = 0
if ma <= 0:
    print("Not Found")
else:
    for i in range(n):
        if m[i] > 0:
            p.append(m[i])
    for i in range(len(p)):
        s += p[i]
    s = s/len(p)
    print(s)