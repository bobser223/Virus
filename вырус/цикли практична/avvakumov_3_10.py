n=int(input())
vidp=0
while n>0:
    ost=n%10
    if n%2==0:
        ost+=1
    else:
        ost-=1
    print (ost)
    vidp=vidp*10+ost
    n//=10
print (vidp)
pass