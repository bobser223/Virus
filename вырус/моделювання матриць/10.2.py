n, m = [int(i) for i in input().split()]
for i in range(1, n*m + 1):
    if (i - 1) % m == 0:
        print()
    print(i, end=" ")