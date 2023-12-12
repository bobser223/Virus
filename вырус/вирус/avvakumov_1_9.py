a, b, n = [int(d) for d in input().split()]
a=abs(a)
b=abs(b)

d=(a*n)
e=(b*n)
g=(e//100)
h=(e%100)
i=(d+g)
if e>=100:
    print(i, h)

else:
    print (d, e)
