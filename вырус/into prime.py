def intoprime(a_num):
    for i in range(2, int(a_num ** (0.5)) + 1):
        if a_num % i == 0:
            a_num = a_num / i
    return int(a_num)

def isprime(a):
    for i in range(2, int(a ** (0.5)) + 1):
        if a % i == 0:
            return False
    else:
        return True

n = 789
print(isprime(n))
print(intoprime(n))
print(isprime(intoprime(n)))