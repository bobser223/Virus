f = open("nabir", encoding="utf-8")
suma = 0
for line in f:
    # print(line)
    d = float(line)
    # print(d)
    suma += d
print(suma)

f.close()
