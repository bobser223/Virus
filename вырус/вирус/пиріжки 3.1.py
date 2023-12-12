
x, y, c = [int(d) for d in input().split()]
d=(y/100)
o=(x*c)
m=(d*c)
if m == int(m):
    h=(o+m)
    h=int(h)
    print(h)
if m >= 1:
    p = ((m*100)//100)
    p=int(p)
    i=m*100
    i=int(i)
    l= ((i-p*100))
    i=(o+p)
    if l != 0:
        print(i, l)
if m < 1:
    if m!=0:
        l = m * 100
        l = int(l)
        print(o, l)

