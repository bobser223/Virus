
n=int(input())
c=0
while n>0:
    ost=n%2
    if ost==1:
        c+=1
    n=n//2
print(c)
