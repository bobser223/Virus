#площа трикутника за 3 сторонами

a = 3
b = 4
c = 51
assert a + b > c and a + c > b and c + b > a


p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)