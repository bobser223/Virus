counter =0

while True:
    a=int(input())
    if a==0:
        break
    if a%2==1:
        counter+=1
print(counter)