# print(max(1, 4, 5, 6, 7, 6))

def max1(*arg):
    if len(arg) == 0:
        return None
    m = arg[0]
    for el in arg[1:]:
        if el > m:
            m = el
    return(m)


print(max1(1, 4, 5, 6, 7, 6))
def f(*arg: tuple):
    print(arg)

f(1, 4, 5, 6, 7, 6)