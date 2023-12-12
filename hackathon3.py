vrz =  "2 + 4.2 * (8.2 - 14 / 3) + (8 + (3 / 2) + 1 / 2)"
def idiot_duz(a):
    suma = 0
    for el in a:
        if el == "(":
            suma += 1
        if el == ")":
            suma -= 1
    if suma == 0:
        return True
    else:
        return False
def count(a):
    a = a.split()
    while True:
        for i in range(len(a)):
            if a[i] == "/":
                a[i] = float(a[i - 1]) / float(a[i + 1])
                a.pop(i - 1)
                a.pop(i)
                break
            if a[i] == "*":
                a[i] = float(a[i - 1]) * float(a[i + 1])
                a.pop(i - 1)
                a.pop(i)
                break
            if a[i] == "//":
                a[i] = float(a[i - 1]) // float(a[i + 1])
                a.pop(i - 1)
                a.pop(i)
                break
            if a[i] == "**":
                a[i] = float(a[i - 1]) ** float(a[i + 1])
                a.pop(i - 1)
                a.pop(i)
                break
        else:
            break
    while True:
        for i in range(len(a)):
            if a[i] == "+":
                a[i] = float(a[i - 1]) + float(a[i + 1])
                a.pop(i - 1)
                a.pop(i)
                break
            if a[i] == "-":
                a[i] = float(a[i - 1]) - float(a[i + 1])
                a.pop(i - 1)
                a.pop(i)
                break
        else:
            break
    return a[0]

def brackets(a):
    first_br = 0
    first_br_another = 0
    while True:
        for i in range(len(a)):
            if a[i] == ")":
                first_br = i
                while a[i] != "(":
                    i -= 1
                    if a[i] == "(":
                        first_br_another = i
                a = a.replace(a[first_br_another: first_br + 1], str(count(a[first_br_another + 1:first_br:1])))
                break
        else:
            break
    return a
def finalcount(a):
    return count(brackets(a))
print(brackets(vrz))
print(finalcount(vrz))




