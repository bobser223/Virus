import math
x, y = [float(d) for d in input().split()]
#x=50.2655
#y=5

#j=(y**2)
#l=(x/math.pi)

#k=(j-l)

#R=(k**0.5)
R=(y**2-x/math.pi)**0.5
print (f"{R: 0.2f}")