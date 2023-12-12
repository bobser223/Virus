def diferent(a):
    od = a % 10
    des = (a // 10) % 10
    sot = (a // 100) % 10
    t = a // 1000
    if od != des and od != sot and od != t and des != sot and des != t and sot != t:
        return True
    else:
        return False

a, b = [i for i in input().split()]

p = []

for i in range(int(a), int(b)+1):
    if diferent(i):
        p.append(i)

print(*p)