N=int(input("кількість рядків"))
A=[]
for i in range(N):
    row=[int(el) for el in input().split()]
    A.append(row)
print(A)