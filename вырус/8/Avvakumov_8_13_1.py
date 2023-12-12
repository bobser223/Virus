mod = 10**8
def fib(a):
    global fibs
    if fibs[a] != 0:
        return fibs[a]
    else:
        f = fib(a - 1) + fib(a - 2)
        fibs[a] = f
        return f

def nsd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, (a % b)
    return a



while True:
    try:
        n, m = [int(el) for el in input().split()]
        d = nsd(n, m)
        N = d
        fibs = [0] * (N + 1)
        fibs[0] = 0
        fibs[1] = 1
        fibs[2] = 2
        fibs[3] = 3
        fibs[4] = 5
        print(fib(d)%mod)
    except:
        break