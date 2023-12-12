def prost(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
            break
    else:
        return True

def reversed(a):
    d = 0
    while a > 0:
        b = a % 10
        d = (10*d) + b
        a //= 10
    return d

m = int(input())
i = 0
n = 1
while (i < m):
    if n != reversed(n) and prost(n) and prost(reversed(n)):
        i += 1
    if i == m:
        if n > 10**6:
            print(-1)
        print(n)
    n += 1
