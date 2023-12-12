n=int(input())
vidp=0
while n>0:
    ost=n%10
    if n%2==0:
        ost+=1
    else:
        ost-=1
    vidp=vidp*10+ost
    n//=10
vidp2=0
while vidp>0:
    ost2=vidp%10
    vidp2 =vidp2*10+ost2
    vidp//=10
print (vidp2)