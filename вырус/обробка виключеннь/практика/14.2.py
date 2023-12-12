s = input()
suma = 0
for c in s:
    if c >= "0" and c <= "9":
        suma += int(c)
print(suma)

suma = 0
for c in s:
    if c.isdigit():
        suma += int(c)
print(suma)

# можна через трай але попереднє краще

suma = 0
for c in s:
    try:
        suma += int(c)
    except ValueError:
        continue
print(suma)

suma = 0
for c in s:
    try:
        suma += int(c)
    except ValueError:
        pass
print(suma)