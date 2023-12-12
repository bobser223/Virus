a, b, x, y, z = [float(d) for d in input().split()]
if y<a and z<b:
    print (1)
elif z<a and y<b:
    print (1)
elif x<a and y<b:
    print (1)
elif y<a and x<b:
    print (1)
elif x<a and z<b:
    print (1)
elif z<a and x<b:
    print (1)
else:
    print (0)
