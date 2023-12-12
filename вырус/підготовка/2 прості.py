def prost(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    else:
        return True

counter = 0
for num in range(1000, 10001):
    if prost(num):
        counter += 1
print(counter)
