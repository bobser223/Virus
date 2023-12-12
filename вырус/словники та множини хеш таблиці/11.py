# слова у рядках розділяються одним або...
# скільки однакових слів

s = "hello  world  hello hello     hello   hello world  forever"
# використаємо словник, ключі - словаб значення-їх кількість
words = s.split()
print(words)
d_words = dict.fromkeys(words,0)
print(d_words)

for word in words:
    d_words[word] += 1
print(d_words)
# for elem in d_words.values():
#     print(elem)
for word, count in d_words.items():
    print(f"Our sentence contains wold '{word}' {count} times ")