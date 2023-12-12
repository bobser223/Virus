s = "hello world"

d = dict.fromkeys([chr(c) for c in range(ord("a"), ord("a") + 26)])
print(d)