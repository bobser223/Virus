n=int(input())
vidp=0
par2=-1
par=0
while n>0:
    ost=n%10
    if ost%2==0:
        par=ost
    else:
        par=0
    par2 += par
    n//=10
if par2!=-1:
    par2+=1
print (par2)