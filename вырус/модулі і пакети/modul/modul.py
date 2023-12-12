# print("module: ", __name__)

# import my_main

def isPrime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':

    print(isPrime(2))
    print(isPrime(27))
    print(isPrime(29))
    print(isPrime(9))