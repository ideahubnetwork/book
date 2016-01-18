from collections import defaultdict

d = defaultdict(list)
d['a'].append('ab')
d['a'].append('acd')
d['a'].append('bef')

print(d)

s = defaultdict(set)
s['a'].add('ab')
s['a'].add('ab')
s['b'].add('b')

print(s)