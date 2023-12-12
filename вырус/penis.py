def fib(n):
    p1 = [0, 1]
    while len(p1) < n:
        m = p1[-1] + p1[-2]
        p1.append(m)
    return int(p1[-1])

def fib1(a):
    global fibs
    if fibs[a] != 0:
        return fibs[a]
    else:
        f = fib(a - 1) + fib(a - 2)
        fibs[a] = f
        return f
N = int(input())
fibs = [0] * (N + 1)
fibs[0] = fibs[1] = 1
fibs[2] = 2
fibs[3] = 3
fibs[4] = 5
if fib1(N) == fib(N):
    print(True)

