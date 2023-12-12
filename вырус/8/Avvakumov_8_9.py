def v13(a):
    b = "0123456789ABCD"
    if a == 0:
        return ""
    else:
        return v13(a // 13) + b[a % 13]

n = int(input())
print(v13(n))