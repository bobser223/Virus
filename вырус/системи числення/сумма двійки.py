a, b = [int(d) for d in input().split()]
p = (1 << a) ^ (1 << b)
print(p)