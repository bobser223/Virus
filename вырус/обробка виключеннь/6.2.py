
a = 3
b = 4
c = 51
def triangleSquare(a, b, c):
    assert a + b > c and a + c > b and c + b > a, "Не виконується рівність трикутника"


    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s
try:
    print(triangleSquare(a, b, c))
except AssertionError as err:
    print("зрада")
    print(err)