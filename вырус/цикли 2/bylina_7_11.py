m=int(input())
p = []

def pr(n, k):
    p = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p1 = ''
    while n > 0:
        p1 = p[n % k] + p1
        n //= k
    return p1
def pal(i):
    if i == i[::-1]:

       return True

for k in range(2, 37):

    if pal(pr(m, k)):
        p.append(k)

if len(p) == 0:
    print("none")
elif len(p) == 1:
    print("unique")
    print(*p)

elif len(p) > 1:
    print("multiple")
    print(*p)

