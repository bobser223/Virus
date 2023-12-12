k=int(input())
i=0

while i<k:
    a=int(input())
    p=a
    i+=1
    if p%2==0:
        a=str(a)+ " is even"
    else:
        a=str(a)+ " is odd"
    print(a)