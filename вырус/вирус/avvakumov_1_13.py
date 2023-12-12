x, y = [float(d) for d in input().split()]
#q=((x**2)+(-2*x*y)+(4*(-y**2)))
#w=(x+5)
#e=(3*(x**2)-(y**2))
#r=(y-7)
#t=(q/w+e/r)
#print (t)
#верх 1
g= (x**2)
h=(2*x*y)
j=(4*(y**2))
q=(g-h+j)
#низ 1
w=(x+5)
#верх 2
k=(3*(x**2))
l=(y**2)
e=(k-l)

r=(y-7)
t=(q/w+e/r)

print (f"{t: 0.3f}")
