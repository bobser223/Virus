m = (int(input()))
n=int(input())
m=max(m,n)
n=min(m,n)
p=1
while p!=0:
    o=p
    p=m-n
    m=p
    n=m
    if p==0:
        print (o)

