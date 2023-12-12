F = {}
MOD = 10 ** 8


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n in F:
        return F[n]

    k = n // 2

    if n % 2 == 1:
        F[n] = (fib(k) * fib(k) + fib(k + 1) * fib(k + 1)) % MOD
    else:
        F[n] = (fib(k) * fib(k + 1) + fib(k - 1) * fib(k)) % MOD

    return F[n]


while True:
    try:
        a, b = map(int, input().split())
        d = gcd(a, b)
        result = fib(d)
        print(result)
    except ValueError:
        print("Некоректний формат введених даних.")
    except KeyboardInterrupt:
        break

