
# def FF(n):
#     if n == 0:
#         return 0
#     if (n % 10) > 0:
#         return n % 10
#     else:
#         return F(n // 10)
cash={0: 0, }
def F(n):
    if n in cash:
        return cash[n]
    if n % 10 > 0:
        f=n%10
        cash[n]=f
        return n % 10
    else:
        f=F(n//10)
        cash[n]=f
        return F(n // 10)
def S(p, q):
    resultat = 0
    for i in range(p, q+1):
        resultat += F(i)
    return resultat


while True:
    p, q = [int(i) for i in input().split()]
    if p < 0 and q < 0:
        break
    print(S(p, q))



