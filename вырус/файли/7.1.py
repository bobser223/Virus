suma = 0
f = open("nabir", encoding="utf-8")
nums = [float(line) for line in f.readlines()]
f.close()

print(sum(nums))

