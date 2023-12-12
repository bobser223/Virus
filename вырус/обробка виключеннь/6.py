#площа трикутника за 3 сторонами

a = 3
b = 4
c = 5
if a + b <= c or a + c <= b or c + b <= a:
    print("трикутник не існує")
else:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)