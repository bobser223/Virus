

# suma = 0
# while True:
#     a = input("Введіть ціле число або стоп: ")
#     if a == "stop":
#         break
#     try:
#         int_a = int(a)
#     except ValueError:
#         print("ЄЄЄЄ, стопе! Введи ціле!!!! ")
#     suma += int_a
# print(suma)

suma = 0
while True:
    a = input("Введіть ціле число або стоп: ")
    try:
        suma += int(a)
    except ValueError:
        if a == "stop":
            break
        print("ЄЄЄЄ, стопе! Введи ціле!!!! ")
print(suma)