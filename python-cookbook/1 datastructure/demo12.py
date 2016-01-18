from collections import Counter

c = Counter('python cookbook')

print(c)    # Counter({'o': 5, 'k': 2, 'p': 1, 't': 1, 'h': 1, 'y': 1, 'c': 1, 'b': 1, 'n': 1, ' ': 1})
print(c.most_common(2))     # [('o', 5), ('k', 2)]