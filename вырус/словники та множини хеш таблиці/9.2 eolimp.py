m = int(input())
n = input().split()

d = {k: n.count(k) for k in n}
for i in d:
    if d[i] > (m // 2):
        print(i)
        break
else:
    print("-1")
