def prost(n:int):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True


a = int(input())
for i in range(a, 2*a - 2):
    if prost(i) and prost(i+2):
        print(i, i+2)