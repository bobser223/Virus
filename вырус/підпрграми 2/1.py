def prost(a):
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return False
            break
    else:
        return True


n = int(input())
print(prost(n))