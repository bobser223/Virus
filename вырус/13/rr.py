f = open("file_13_5")
lst = [float(i) for i in f.readlines()]
f.close()
def maxx(lst):
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

print(maxx(lst))