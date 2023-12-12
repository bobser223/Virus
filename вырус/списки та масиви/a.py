N=int(input())
lst = [int(el) for el in input().split()]
print (N)
print (*lst)
for el in lst:
     if el >=0:
         el+=2
print (*lst)
for i in range(len(lst)):
    if lst[i] >= 0:
        lst[i] += 2
print (*lst)
#теж саме що і
for i in range(N):
    if lst[i] >= 0:
        lst[i] += 2
print (*lst)
n=[]
for el in lst:
     if el >=0:
         n.append(el+2)
     else:
          n.append(el)
nrint(n)