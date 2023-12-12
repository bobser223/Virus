p = [int(el) for el in input().split()]
print(p)
p2 = {}
for i in range (0,len(p),2):
    p2[p[i]] = p[i+1]
print(p2)
suma = 0
for i in range((max(p2)) + 1):
    try:
        suma += p2[i] * i
    except KeyError:
        continue
print(suma)

p = [int(el) for el in input().split()]
ma = int(input())
print(p)
p2 = {}
for i in range (0,len(p),2):
    p2[p[i]] = p[i+1]
print(p2)
suma = 0
for i in range(ma + 1):
    try:
        suma += p2[i] * i
    except:
        continue
print("в гаманці: ", suma)
