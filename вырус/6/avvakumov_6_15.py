# слово чемпіон
n = input()
p = ""
for el in n:
    if el in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ":
        p += el
p = p.lower()
print(p)
s = p.split()
p1 = ""
for el in s:
    if el == el[::-1]:
        p1 += el
n1 = max(p1,key=len)
print(n1)

