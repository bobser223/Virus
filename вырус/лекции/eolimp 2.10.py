x=int(input())
y=x//100
z=x//10%10
v=x%10
if y > v:
    print (int(y))
elif v>y:
    print (int(v))
if y==v:
    print ("=")
