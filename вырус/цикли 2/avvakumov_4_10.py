n=int(input())
d=1
s=0
l=0

if n==1:
    for i in range(100, 1000):
        od = i % 10
        des = (i // 10) % 10
        sot = i // 100
        if od%2==0 and des%2==0 and sot%2==0:
            d=i
            s+=d
    print (s)
if n==2:
    for i in range(100, 1000):
        od = i % 10
        des = (i // 10) % 10
        sot = i // 100
        if od>des>sot:
            l+=1

    print (l)
if n==3:
    for i in range(100, 1000):
        od = i % 10
        des = (i // 10) % 10
        sot = i // 100
        if od%2==1 and des%2==1 and sot%2==1:
            d=i
            s+=d
    print (s)
if n==4:
    for i in range(100, 1000):
        od = i % 10
        des = (i // 10) % 10
        sot = i // 100
        if od<des<sot:
            l+=1

    print (l)
if n==5:
    for i in range(100, 1000):
        od = i % 10
        des = (i // 10) % 10
        sot = i // 100
        if i==(od**3)+(des**3)+(sot**3):

            s += i
    print (s)

if n==6:
    for i in range(100, 1000):
        od = i % 10
        des = (i // 10) % 10
        sot = i // 100
        if od!=des and od!=sot and sot!=des:
            l+=1

    print (l)
