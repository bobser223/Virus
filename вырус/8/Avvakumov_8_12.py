def F(x, n, m):
    if n == 0:
        return 1
    if n % 2 == 1:
        return (x * F(x * x % m, n // 2, m)) % m
    else:
        return F(x * x % m, n // 2, m)

i = 1
while True:
    k, n, t = [int(i) for i in input().split()]
    if k == 0 and n == 0 and t == 0:
        break

    m = 10 ** t
    res = F(k % m, n, m)
    print(f"Case #{i}: {res}")
    i += 1