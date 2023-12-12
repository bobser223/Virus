n=int(input())
N=n
pol=0
while N>0:
    ost=N%10
    pol=pol*10+ost
    N//=10

i=1
if pol==n:
    print (0)
else:
    while n!=pol :
        d=n+pol
        n=d
        N=n
        pol=0
        while N>0:
            ost=N%10
            pol=pol*10+ost
            N//=10

        if d==pol:
           continue
        i+=1
print (i)