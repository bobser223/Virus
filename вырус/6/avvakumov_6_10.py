n = input()
p = ""
for el in n:
    p += el
    if el in "qwertyuiopasdfghjklzxcvbnm":
        p += el
print(p)