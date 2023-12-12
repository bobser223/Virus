
s = input()
p = ""

p += s[2]
p += s[6]
p += s[10]
print(p)

p = ""

p += s[0]
p += s[len(s)-2]
p += s[len(s)-1]
print(p)

p = ""

for el in s[:7:1]:
    p += el
print(p)

p = ""

for el in s[4::1]:
    p += el
print(p)

p = ""

for el in s[1::2]:
    p += el
print(p)

print(len(p))

p = ""

for el in s[::-1]:
    p += el
print(p)
