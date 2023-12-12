n = input()
p = ""
for i in range(len(n)):
    p += n[i]
    if n[i] in "aeiouy":
        p += n[i]
print(p)
