s = "hello  world  hello hello     hello   hello world  forever"
words = s.split()
d_words = {
   word: words.count(word) for word in words
}
print(d_words)

for word, count in d_words.items():
    print(f"Our sentence contains wold '{word}' {count} times ")