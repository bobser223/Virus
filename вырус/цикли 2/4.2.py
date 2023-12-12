n=int(input())
od=1
b=1
o=0
y=1
if n==1:
    for i in range (10, 100):
        od=i%10
        b=i//10
        if od<b:
            o+=1
    print (o)
elif n==2:
    for i in range (10, 100):
        od=i%10
        b=i//10
        if od>b:
            o+=1
    print (o)
elif n==3:
    for i in range (10, 100):
        od=i%10
        b=i//10
        if (od%2==0 and b%2==0) or (od%2!=0 and b%2!=0):
            o+=1
    print (o)
elif n==4:
    for i in range (10, 100):
        od=i%10
        b=i//10
        if od==b:
            t=od+b
            t+=t
    print(t)
elif n==5:
    for i in range (10, 100):
        od=i%10
        b=i//10
        if od%2==0 and b%2==0:
            t=od+b
            t+=t
    print (t)
elif n==6:
    for i in range (10, 100):
        od=i%10
        b=i//10
        if od%2!=0 and b%2!=0:
            y=od+b
            y+=y
    print (y)