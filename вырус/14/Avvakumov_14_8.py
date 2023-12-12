lst = []
runtimeerror = 0
typeerror = 0
valueerror = 0

while True:
    a = input()
    if a == "досить":
        break
    try:
        a = float(a)
    except ValueError:
        print("введіть число")
        continue
    try:
        if a > 9:
            runtimeerror += 1
            raise RuntimeError
    except RuntimeError:
        continue
    try:
        if a < 0:
            typeerror += 1
            raise TypeError
    except TypeError:
        continue
    try:
        if 0 < a < 9 and int(a) != a:
            valueerror += 1
            raise ValueError
    except ValueError:
        continue
    lst.append(int(a))
print(*lst)
print(f"RuntimeError: {runtimeerror}")
print(f"TypeError: {typeerror}")
print(f"ValueError: {valueerror}")