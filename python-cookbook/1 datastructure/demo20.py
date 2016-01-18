from collections import ChainMap

dict1 = {
    'a': 3,
    'b': 4
}

dict2 = {
    'b': 5,
    'c': 6
}

dict3 = ChainMap(dict1, dict2)
print(dict3['b'])

dict4 = dict(dict1, **dict2)
print(dict4['b'])