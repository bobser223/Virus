n = "pentium pro"
print(n.capitalize())

n = "Pentium Pro"

print(n.lower())

n = "pentium pro"

print(n.upper())

print(n.title())

#Найважливіші!!!!!!!!!!!!!!!!!

n = "   pentium   pro   "

print(n.split())
print(n.split(" "))

n1 = "bobserpidor"
print(n1.split("p"))

n2 = "avvakumov@knu.ua"
print(n2.split("@"))
########################################
d = ["mechmat", "knu", "ua"]
s = d[0]
for el in d[1:]:
    s += "." + el
print(s)
########################
s = ".".join(d)