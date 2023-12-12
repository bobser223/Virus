def pol(a):
    a = str(a)
    if a == a[::-1]:
        return True
    else:
        return False

counter = 0

for num in range(10000, 100000):
    num2 = num**2
    if pol(num) and pol(num2):
        counter += 1
print(counter)