n=int(input())
m=1
p=1
while m<=n:
    if (p%2!=0) and (p%3!=0) and (p%5!=0):
        print (p)
        m+=1
    p+=1