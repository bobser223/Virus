def nsd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b

    return a
def nsk(a,b):
    c = (a*b) / nsd(a,b)
    c = int(c)
    return c

#  Задано два натуральних числа A та B. Знайти кількість таких пар чисел (P, Q), що для них A є НСД(P, Q), а B - НСК(P, Q).
#
# Вхідні дані
#    У єдиному рядку два натуральних числа A та B (A < 105, B ≤ 106).

a, b = [i for i in input().split()]
i = 0
for p in range(10000):
    for q in range(10000):
        if nsd(p,q) == a and nsk(p,q) == b:
            i += 1
print(i)


