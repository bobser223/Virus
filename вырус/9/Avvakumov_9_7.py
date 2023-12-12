l = input()
st = input()
p = {}
for el in st:
    if el in p:
        p[el] += 1
    if el not in p:
        p.update({el: 1})

for i in p:
    if p[i] % 2 == 1:
        print(i)
        break


else:
    print("Ok")