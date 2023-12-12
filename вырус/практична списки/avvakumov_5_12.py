n = int(input())
m = [int(d) for d in input().split()]
p = [x for x in m if n.count(x)>1]


print(*p)