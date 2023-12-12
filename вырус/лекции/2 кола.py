x1,y1,r1,x2,y2,r2 = [float(d) for d in input().split()]
z= ((x2-x1)**2+(y2-y1)**2)**0.5
if x1==x2 and y1==y2 and r1==r2:
    print (1)
elif (r1+r2) <z:
    print(0)
elif (r1+r2)==z:
    print (1)
elif (r1+r2)>z:
    print (2)
5