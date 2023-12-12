def fact(a):
    if a == 0 or a == 1:
        return 1
    if a == 2:
        return 2
    else:
        return a * fact(a - 1)

n = int(input())
print(fact(n))