x, y = [float(d) for d in input().split()]
q= (2*(x*y))

j=(x**2)
k=(y**2)

w= ((j+k)**0.5)

e=((x+y-1)**2)
r= (x*y)


t=(q/w-e/r)

print (f"{t: 0.3f}")
