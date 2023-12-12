f = open("mn 1")
mn1 = f.readline()
f.close()
f = open("mn 2")
mn2 = f.readline()
f.close()
mn1 = mn1.split()
mn2 = mn2.split()
# mn1.reverse()
# mn2.reverse()
# def pohidna1(mn):
#     for i in range(1, len(mn)):
#         mn[i - 1] = int(mn[i]) * int(i)
#     return mn

def pohidna(mn):
    mn.reverse()
    for i in range(len(mn)):
        mn[i] = int(mn[i]) * (int(i))
    mn.pop(mn[0])
    mn.reverse()
    return mn

print(pohidna(mn1))
print(pohidna(mn2))

# def suma:
