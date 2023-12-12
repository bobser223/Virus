
def fib(a):
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

# [1 1 0 0 0 0 0 0 0 0 0  0 0 0 0 0 0 0 0 ]
#  0 1 2 3 4 5 6 7 8 9 10 11
print(fib(N))