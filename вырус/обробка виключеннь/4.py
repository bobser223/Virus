try:
    lst = [1, 2, 3]
    print(lst[5])
    d = {"first": 1, "second": 2,}
    print(d["third"])
# except IndexError:
#     print("Помилка індексу")
# except KeyError:
#     print("Помилка ключа")
except LookupError:
    print("Помилка ключа або індексу")
# except BaseException: ==== except: Тімлід дасть пизди
#     print("problem")