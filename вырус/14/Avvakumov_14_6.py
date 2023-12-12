#Розв’язати квадратне рівняння ax^2+bx+c=0. Оформити перевірку вхідних даних (що рівняння є квадратним і має розв’язок на множині дійсних чисел) за допомогою оператора assert
def solution(a, b, c):
    solution1 = ((b * (-1)) + (b ** 2 - 4 * a * c) ** (0.5)) / (a * 2)
    solution2 = ((b * (-1)) - (b ** 2 - 4 * a * c) ** (0.5)) / (a * 2)
    if solution1 == solution2:
        return solution1
    else:
        return solution1, solution2
try:
    a, b, c = [int(i) for i in input().split()]
    assert b**2 - 4*a*c >= 0 and a != 0
    print(solution(a, b, c))
except AssertionError:
    print("раціональних коренів не існує")
except ValueError:
    print("Ви ввели значення, які не можуть бути коефіцієнтами квадратного рівняння")






























# except:
# assert b**2 - 4*a*c >= 0 or a != 0
# except AssertionError:
#     print("це не квадратне рівняння")
# solution1 = ((b*(-1)) + (b**2 - 4*a*c)**(0.5)) / (a*2)
# solution2 = ((b*(-1)) - (b**2 - 4*a*c)**(0.5)) / (a*2)
# if solution1 == solution2:
#     print(solution1)
# else:
#     print(solution1, solution2)

