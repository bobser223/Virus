#x= input()
#y=x%2
#сумма першого і дркгої цифри 2 значного числа двозначне число
#x, y = [float(d) for d in input().split()]
x=int(input())
y=x//10
z=x-y*10
if (y+z) >= 10:
    print (y+z)