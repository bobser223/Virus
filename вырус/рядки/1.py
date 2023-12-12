s = "Hello world"
#    012345678910
for ch in s:
    print(ch)
for i in range(len(s)):
    print(i, ":", s[i])
# рядок це кортеж а не список(незмінюваний)
s1 = s * 2
print(s1)
p1 = "Hello"
p2 = "world"
p3 = p1 + " " + p2 + '!'
print(p3)
# якщо потрібно лапки всередині то використовуємо інші
c = 'hotel "California"'
c1 = "hotel 'California'"
print(c, c1)
m = ("Володя"
     " мудак"
     " і"
     " чмо")
multilineM ="""
Володя
мудак 
і
чмо"""
print(m, multilineM)
