# робочий код для фібаначі стирив, бо ваш, як і мій (він == вашому, я паравіряв) не працює з великими числами,
F = {}
MOD = 10 ** 8
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
def nsd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, (a % b)
    return a



while True:
    try:
        n, m = [int(el) for el in input().split()]
        d = nsd(n, m)
        print(fib(d))
    except:
        break