a, b, c = [float(d) for d in input().split()]
#if a and b and c > 0:
    #if (a+b)>c and (a+c)>b and (b+c)>a:
        #Eprint()
cond = (a>0 and b>0and c>0
        and a+b>c
        and c+b>a
        and c+a>b)
print (cond)