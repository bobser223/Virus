n=int(input())
k=int(input())
bit=n%k
powk=1
o=0
while n>o:
    ost=n%10
    o+=bit*powk
    powk=powk*k
    n//=10
print (o)