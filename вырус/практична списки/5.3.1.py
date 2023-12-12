n=int(input())
m=0
counter=0
nl = [float(el) for el in input().split()]
r=[]
for i in range (2,n,3):
    el = nl[i]
    if el>0:
        counter+=1
        m +=el

print (counter , m)