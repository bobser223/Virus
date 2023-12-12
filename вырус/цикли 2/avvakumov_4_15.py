n=int(input())
odd=0
o=0
b=True
for i in range (1*(10**(n-1)), 10**n):
    c=i
    while c>0:
        odd=c%10
        if odd%2==0:
            b=False
            break
        c//=10
    if b==True:
        i+=1
print (i)