def kvadr(k):
    if (int(k**0.5))**2 == k or k == 2:
        return True
    else:
        return False

def five(a):
    while a > 4:
        if a % 5 != 0:
            return False
        a //= 5
    return True


def prost(n:int):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True


lst = [int(el) for el in input().split()]
lstk = []
lstp = []
lstf = []
for i in lst:
    if kvadr(i):
        lstk.append(i)
    if prost(i):
        lstp.append(i)
    if five(i):
        lstf.append(i)
print (lstf, lstp, lstk)

def five(a):
    while a > 4:
        if a % 5 != 0:
            return False
        a //= 5
    return True
