# Пароль містить маленькі латинські латинські літери
#
# Пароль містить великі латинські літери
#
# Пароль містить цифри
#
# Символи: ! " # $ % & ' ( ) * +
#
# Довжина пароля не менше 8 символів
n = input()
i = 0
c = 0
for el in n:
    if el in "qwertyuiopasdfghjklzxcvbnm":
        c += 1
if c > 0:
    i += 1
#
c = 0
#
for el in n:
    if el in "QWERTYUIOPASDFGHJKLZXCVBNM":
        c += 1
if c > 0:
    i += 1
#
c = 0
#
for el in n:
    if el in "1234567890":
        c += 1
if c > 0:
    i += 1
#
c = 0
#
for el in n:
    if el in "!#$%&'()*+" or el == '"':
        c += 1
if c > 0:
    i += 1
#
if len(n) >= 8:
    i += 1
print(i)