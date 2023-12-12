
def maxelcount(a):
    f = [0] * 10
    while a > 0:
        last = a % 10
        f[last] += 1
        a //= 10
    print(f)
    maxn = 0
    maxc = -1
    for i,el in enumerate(f):
        if el > maxc:
            maxc =el
            maxn = i
    return maxn, maxc

############################ main program
# f = [0]*10
# while a > 0:
#     last = a % 10
#     f[last] += 1
#     a //= 10
# print(f)
# a = 12341231453423
print(maxelcount(12341231453423))