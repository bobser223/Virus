n = input()
i = 0

for e in range(1, len(n)):
    if n[e] in "*/+-%":
        if n[e] == n[e-1]:
            continue
        i += 1
print(i)