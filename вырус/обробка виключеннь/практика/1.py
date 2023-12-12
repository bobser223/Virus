
a = input()
try:
    a = int(a)
except ValueError:
    print(f"число {a} не ціле")