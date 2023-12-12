n=int(input())
suma=0
dobu=1

while n > 0:
    last = n%10
    suma+=last
    dobu*=last
    n = n // 10
dil=dobu/suma
print (f"{dil:0.3f}")