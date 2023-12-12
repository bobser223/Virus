# 1 3 12 89 6 1
seq = [0, 1, 3, 12, 84, 6, 1]
try:
    maxr = seq[1] / seq[0]
    for i in range(2, len(seq)):
        curr = seq[i] / seq[i - 1]
        if curr > maxr:
            maxr = curr
    print(maxr)
except ZeroDivisionError:
    print("послідовність містить 0")
# print(maxr)

seq = [ 1, 3, 12, 84, 6, 1]
maxr = 0
try:
    for i in range(1, len(seq)):
        curr = seq[i] / seq[i - 1]
        if curr > maxr:
            maxr = curr
except ZeroDivisionError:
    print("послідовність містить 0")
else:
    print(maxr)