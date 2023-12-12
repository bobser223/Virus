
def lenn(lst):
    try:
        counter = 0
        i = 0
        while True:
            a = lst[i]
            counter += 1
            i += 1
    except IndexError:
        return counter



def summa(lst):
    try:
        i = 0
        a = 0
        while True:
            a += lst[i]
            i += 1
    except IndexError:
        return int(a)




def maxdiv(lst):
    try:
        pplus = []
        i = 0

        while True:
            a = lst[i]
            if a > 0:
                pplus.append(a)
            i += 1
    except IndexError:
        pass
    try:
        pminus = []
        i = 0

        while True:
            a = lst[i]
            if a < 0:
                pminus.append(a)
            i += 1
    except IndexError:
        pass
    try:
        if lenn(pplus) == 1 and lenn(pminus) == 1:
            return max(pminus[0]/pplus[0], pplus[0]/pminus[0])
        elif lenn(pminus) > 1 and lenn(pplus) > 1:
            maxminus = min(pminus)
            minminus = max(pminus)
            maxplus = max(pplus)
            minplus = min(pplus)
            # if maxplus / minplus >= maxminus / minminus:
            #     return maxplus / minplus
            # else:
            #     return maxminus / minminus
            return max(maxminus / minminus, maxplus / minplus)
        elif lenn(pminus) == 0 or lenn(pminus) == 1:
            maxplus = max(pplus)
            minplus = min(pplus)
            return maxplus / minplus
        elif lenn(pplus) == 0 or lenn(pplus) == 1:
            maxminus = min(pminus)
            minminus = max(pminus)
            return maxminus / minminus
    except ZeroDivisionError:
        return "Хто догадався ввести 0"

#
try:
    lst = [float(i) for i in input().split()]
    print(summa(lst))
    print(lenn(lst))
    print(maxdiv(lst))
except ValueError:
    print("Це повідомлення появляється коли программа провалила манкі тест")
# lst = [1, 2, 3, 4, 5, 6]



