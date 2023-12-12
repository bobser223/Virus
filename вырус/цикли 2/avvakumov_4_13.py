n=int(input())
r=0
for i in range(10,100):
    od=i%10
    des=(i // 10) % 10
    o=i*n
    odn = o % 10
    desn = (o // 10) % 10
    if (od+des)==(odn+desn):
        r+=1
print(r)