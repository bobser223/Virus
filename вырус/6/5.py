n = input()
p = n[0]
# for i in range(len(n)):
#     if n[i-1] == n[i]:
#         continue
#     p += n[i]
for el in n[1:]:
    if el != p[-1]:
        p += el
print(p)
