s = "Hello  world    Hello world Hello Hello"
# кількість слів(різних)
s = s.lower()
w = s.split()
uniq_w = set(w)
print("кількість унікальних слів у рядку =", len(uniq_w))