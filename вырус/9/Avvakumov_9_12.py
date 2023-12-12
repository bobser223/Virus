n = set(input()) #abrakadabra
m = set(input()) #kabak
for el in m:
    if el not in n:
        print("No")
        break
else:
    print("Ok")