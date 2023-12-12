# опишеми фцію що шукає більше з 2х чисел
def max2(a,b):
    if a > b:
        return a
    else:
        return b


m = max2(41,5)
print(m)

m = max2(max2(41,5),13821248)
print(m)