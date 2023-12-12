def comb(a):
    global p
    if a == 1:
        return 1
    else:
        p.append(a)
        return comb(a-1),
p = []
print(comb(12))