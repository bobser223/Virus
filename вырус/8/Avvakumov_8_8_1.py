def st(a):
    p = ""
    p1 = ""
    while a > 0:
        p = str(a % 2) + p
        a //= 2
    for i in p:
        if i == '1':
            p1 = p1 + "SX"
        if i == '0':
            p1 = p1 + "S"
    p1 = p1[2:]
    return p1
n = int(input())
print(st(n))