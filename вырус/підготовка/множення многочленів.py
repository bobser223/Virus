f = open("mn 1")
mn1 = f.readline()
f.close()
f = open("mn 2")
mn2 = f.readline()
f.close()
mn1 = list(map(int, mn1.split()))
mn2 = list(map(int, mn2.split()))
mn1.reverse()
mn2.reverse()
print()
mn3 = [0]*(len(mn1) + len(mn2) - 1)
for i in range(len(mn1)):
    for j in range(len(mn2)):
        koef = mn1[i] * mn2[j]
        step = i + j
        mn3[step] = mn3[step] + koef
mn3.reverse()
print(mn3)

