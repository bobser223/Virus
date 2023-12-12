d = {
    "Hello": "World",
     '2333': "3",
     "3": 3,
 }
for key in d:
    print(key, d[key])

for item, val in d.items():
    print(item, val)

for item in d.items():
    print(item)

print(len(d))

print(min(d))

print(max(d))