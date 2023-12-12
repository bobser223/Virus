def step(a):
    if a == 0:
        return 1
    if a == 1:
        return 2
    if a == 2:
        return 4
    else:
        return step(a-1) * 2

n = int(input())
print(step(n))