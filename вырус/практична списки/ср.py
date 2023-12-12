n = 0
# for i in range(100, 1000):
#     od=i%10
#     des=(i//10)%10
#     sot=i//100
for od in range (10):
    for des in range(10):
        for sot in range(10):

            sum=od + des + sot
            ods=sum%10
            dess=(sum//10)%10
            if ods == 7 or dess ==7:
                n+=1
print(n)