s = "hello  world  hello hello     hello   hello world  forever"
words = s.split()
d_words = {word: words.count(word) for word in words}
print(d_words)

max_word = ""
max_count = 0

for w, c in d_words.items():
    if max_count < c:
        max_word = w
        max_count = c

print(f"Слово{max_word}зустрічається найбільше ксть разів{max_count}")