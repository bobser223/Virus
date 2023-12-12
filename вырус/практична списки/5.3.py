n=int(input())
m=0
counter=0
nl = [float(el) for el in input().split()]
r=[]
for i in range (n):
    if i%3==0 and i>0:
        r.append(nl[i])
for i in range (len(r)):
    m+=r[i]
print (len(r),m )