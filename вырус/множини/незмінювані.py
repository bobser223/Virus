# frozenset
s = {1, 2, 3, 4}
frs = frozenset({4, 5, 6})
print(s)
print(frs)

# frs.add(23)
s.add(23)

print(s)
print(frs)

s.discard(23)
print(s)

news = s | frs
print(news)

news = frs | s
print(news)
unfrs = set(frs)
print(unfrs)

