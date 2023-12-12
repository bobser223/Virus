f = open("mn 1")
mn1 = f.readline()
f.close()
f = open("mn 2")
mn2 = f.readline()
f.close()
mn1 = mn1.split()
mn2 = mn2.split()
mn1.reverse()


uigiuyg
mn2.reverse()

if len(mn1) == len(mn2):
    mn3 = [0] * len(mn2)
    for i in range(len(mn1)):
        for j in range(len(mn2)):
            if i == j:
                koef = int(mn1[i]) + int( mn2[j])
                mn3[i] = koef
    print(mn3)
