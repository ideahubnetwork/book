from collections import OrderedDict
import sys

dict1 = {
    'name': 'wang',
    'age': 22
}

dict2 = OrderedDict()
dict2['name'] = 'wang'
dict2['age'] = 22

print(dict1, sys.getsizeof(dict1))
print(dict2, sys.getsizeof(dict2))