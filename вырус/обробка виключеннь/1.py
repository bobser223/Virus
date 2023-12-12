

try:
    f = open("piska")
    n = float(f.readline())
    k = 12 / n
    print(k)
    print("програма завершилась природним чином")
    f.close()
except ZeroDivisionError:
    print("заебал ты меня со своим делением на 0, хуй себе на лоб пришей")
except FileNotFoundError:
    print("файл вкрали окупанти в львові")
except ValueError:
    print("тебя что по обьявлению набрали, на буквы делить нельзя")
else:
    print("виконується коли немає виключної синуації")
finally:
    print("цей шматок коду виконується завжди")