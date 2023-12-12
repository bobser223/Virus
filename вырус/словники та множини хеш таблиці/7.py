d = {
    "Hello": "World",
     3: "3",
     "3": 3,
 }

if "Hello" in d:
    print(d["Hello"])
else:
    print("None")

print(d.get("2343243242", "penis"))
print(d.get("Hello", "penis"))