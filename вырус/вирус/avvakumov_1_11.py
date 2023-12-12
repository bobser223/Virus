a, b, c,d,f = [float(d) for d in input().split()]
#периметр 1
P=(a+b+f)
p=(P/2)
#периметр 2
O=(d+c+f)
o=(O/2)
#герон 1
s=((p*(p-a)*(p-b)*(p-f))**0.5)
#герон 2
S=((o*(o-d)*(o-c)*(o-f))**0.5)
#загальна площа
pl=(S+s)
print (f"{pl: 0.4f}")
