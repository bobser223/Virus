def mnoz(a):
    if a == 0:
        return ""
    if a % 2 == 0:
        return mnoz(a // 2) + "S"
    else:
        return mnoz(a // 2) + "SX"


n = int(input())
print(mnoz(n)[2:])
