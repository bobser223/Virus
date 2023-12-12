n = input()
b = int(input())
p = ""
# 65 90
for el in n:
    elp = ord(el) - b
    if elp < 65:
        elp = 90 - (65 - elp) + 1
    p += chr(elp)
print(p)