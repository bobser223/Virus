# ord - номер символу в таблиці кодування
# chr - символ по номеру
print(ord("A"))
print(chr(99))
print(chr(ord("A")))
print(ord(chr(99)))
# за веденною з клавіатури латинською літерою вивести її велику літеру
s = input('Введіть малу латинську літеру')


# S = chr(ord(s) - 32) в аскі працює, але в інших таблицях хз
S = chr(ord(s) - (ord("a") - ord("A")))

print(S)




