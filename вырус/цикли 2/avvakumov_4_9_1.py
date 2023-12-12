n=(int(input()))
lst=[int(el) for el in input().split]
while n>=0:
    r=lst(n-1)
    if r%2==0:
        print(str(r)+" is even")
    else:
        print(str(r) + " is odd")

    n=n-1

