N = int(input())
lst = input().split()

d = {}
for el in lst:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1
print(d)
p = []
for num, count in d.items():
    if count == 1:
        p.append(num)
print(p)

###########################

for el in lst:
    if lst.count(el) == 1:
        print(el, end=" ")

########################
N = int(input())
lst = input().split()

d = {}
for el in lst:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1

print(d)

# for el in lst:
#     if d[el] == 1:
#         print(el, end=" ")
