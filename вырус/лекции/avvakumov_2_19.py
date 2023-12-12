x=int(input())
y=x//100
z=x//10%10
v=x%10
if y!=z and y!=v and z!=v:
    print ("YES")
else:
    print ("NO")