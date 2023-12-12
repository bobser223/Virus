import math
######### a ############
def a(file):
    f = open(file, "rt")
    a = f.readlines()
    f.close()
    i = 0
    for num in a:
        if int(num) % 2 == 0:
            i += 1
    return i


print(a("file_13_5"))

########### b #########

def b(file):
    f = open(file, "rt")
    a = f.readlines()
    f.close()
    counter = 0
    for num in a:
        if math.pow(int(num), 0.5) % 2 == 1:
            counter += 1
    return(counter)



print(b("file_13_5"))

########### c ############
#c)    різниці між найбільшим парним і найменшим непарним числами з компонент;

def c(file):
    f = open(file, "rt")
    a = [float(i) for i in f.readlines()]
    f.close()
    par = []
    nepar = []
    for num in a:
        if num % 2 == 0:
            par.append(num)
    for num in a:
        if num % 2 == 1:
            nepar.append(num)
    return int(max(par) - min(nepar))
print(c("file_13_5"))



################## d #######################


def d(file):
    f = open(file)
    lst = [float(i) for i in f.readlines()]
    f.close()
    ma = 0
    m = 1
    for i in range(len(lst)-1):
        if lst[i+1] > lst[i]:
            m += 1
        if i == len(lst)-2 and m > 1:
            if m > ma:
                ma = m
        if lst[i+1] <= lst[i] and m != 1:
            if m > ma:
                ma = m
            m = 1

    return ma

print(d("file_13_5"))

################# d2 ################
def dd(file):
    f = open(file)
    lst = [float(i) for i in f.readlines()]
    f.close()
    ma = 0
    m = 1
    for i in range(len(lst)-1):
        if lst[i+1] > lst[i]:
            m += 1
        else:
            if m > 1:
                ma = max(ma, m)
            m = 1
    if m > 1:
        ma = max(ma, m)

    return ma

print(dd("file_13_5"))



