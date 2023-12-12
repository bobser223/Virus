a = int(input())
b = int(input())
def mnoz(a, b):
    if b == 0:
      return 0
    else:
       return mnoz(a, b-1) + a

print(mnoz(a, b))