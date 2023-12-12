# n1=int(input())
m1= [int(d) for d in input().split()]
# n2=int(input())
m2= [int(d) for d in input().split()]

m3=m1
m1=tuple(m1)
m2=tuple(m2)

for i in range(len(m1)+1):
    for l in range (len(m2)):
        if m1[i] == m2[l]:
            m3.pop(i)
print


