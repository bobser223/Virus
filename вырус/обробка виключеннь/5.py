try:
    lst = [1, 2, 3]
    print(lst[5])
    d = {"first": 1, "second": 2,}
    print(d["third"])

except LookupError as error: # error змінна з інфою про конкретну помилку
    print("Помилка ключа або індексу: ")
    if type(error) == KeyError:
        print("KeyError")
    if type(error) == IndexError:
        print("IndexError")