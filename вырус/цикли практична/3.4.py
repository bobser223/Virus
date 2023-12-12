n=int(input())
#kilkist=1
counter = 0
i=1
if n == 0:
    counter +=1
else:
    while n > 0:
        counter += 1
        n = n // 10
    print(counter)