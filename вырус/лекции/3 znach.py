x=int(input())
y=x//100
z=x//10%10
v=x%10
if y or z or v ==2:
    if x % 2 ==0:
        if y +z +v== 18:
           print (true)