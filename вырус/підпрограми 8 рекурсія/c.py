k, n = [i for i in input().split()]
n = int(n)
k = int(k)
def C(k, n):
    if n == k or n == 0:
        return 1
    else:
        return C(k-1, n-1) + C(k-1, n)
print(C(k,n))

for k in range(k):
