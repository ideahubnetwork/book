table = [
    {'name': 'wang', 'age': 21},
    {'name': 'jing', 'age': 20},
    {'name': 'tian', 'age': 22},
    {'name': 'yan', 'age': 23}
]

table = sorted(table, key = lambda x: x['age'])
for i in table:
    print(i)
