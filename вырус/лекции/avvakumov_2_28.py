n,p,q,k = [float(d) for d in input().split()]
#кількість квартир в підїзді
z=(n/p)
#кількість квартир на поверсі
v=z/q
if k<=z and k<=v:

    print (1,1)
elif k<=2*z and k<=2*v:

    print (2,2)
elif k<=3*z and k<=3*v:

    print (3,3)
elif k<=4*z and k<=4*v:

    print (4,4)
