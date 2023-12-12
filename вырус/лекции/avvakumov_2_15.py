a, b, c = [float(d) for d in input().split()]
#a*x**2+b*x+c=0
x=(-b + (b**2-4*a*c))/(2*a)
y=(-b - (b**2-4*a*c))/(2*a)
x = int (x)
y = int (y)
d=(b**2-4*a*c)
# if d == 0 :
#     print ("One root:",x)
# elif d == 0:
    print ("One root:",y)
if x==y:
    print("One root:", x)
elif d < 0:
    print ("No roots")
else:
    print ("Two roots:", y, x)