n = input()
p = ""
p1 = ""
for el in n:
    if el in "qwertyuiopasdfghjklzxcvbnm":
        p += el
for el in n[::-1]:
    if el in "qwertyuiopasdfghjklzxcvbnm":
        p1 += el
if p1 == p:
    print("YES")
else:
    print("NO")
