
from os import walk
# print(names)
def sum(names):
    names = " ".join(names)
    names = names.split()
    # print(names)
    nums = " "
    for name in names:
        for path in walk("."):
            for file in path[2]:
                if file == name:
                    f = open(file)
                    nums2 = f.readlines()
                    f.close()
                    nums2 = " ".join(nums2)
                    nums2 = nums2.split()
                    nums2 = " ".join(nums2)
                    nums += " " + nums2
    nums = nums.split()
    suma = 0
    try:
        for num2 in nums:
            if num2 in " ":
                continue
            num2 = int(num2)
            suma += num2
    except ValueError:
        return "Ви ввели не цілі числа або літери"
    return suma
try:
    f = open("context.txt")
    names = f.readlines()
    f.close()
    print(sum(names))
except FileNotFoundError:
    print('Файлу "context.txt" в цій папці на жаль не існує')
