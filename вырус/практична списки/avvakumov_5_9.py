a,b,c,d = [int(d) for d in input().split()]
p=[]
if a >= b and c >= d:
    for el in range(b, a + 1):
        for ele in range(d, c + 1):
            dob = el*ele
            p.append(dob)
    print(len(set(p)))
elif b >= a and d >= c:
    for el in range(a, b + 1):
        for ele in range(c, d + 1):
            dob = el*ele
            p.append(dob)
    print(len(set(p)))
elif b >= a and c >= d:
    for el in range(a, b + 1):
        for ele in range(d, c + 1):
            dob = el*ele
            p.append(dob)
    print(len(set(p)))
elif a >= b and d >= c:
    for el in range(b, a + 1):
        for ele in range(c, d + 1):
            dob = el*ele
            p.append(dob)
    print(len(set(p)))