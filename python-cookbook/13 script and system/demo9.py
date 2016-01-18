import os
import sys

def remove(path='.'):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.pyc'):
                file = os.path.join(dirpath, filename)
                os.remove(os.path.join(dirpath, filename))
                print(os.path.abspath(file), 'cleaning...')

if len(sys.argv) == 2:
    remove(sys.argv[1])
elif len(sys.argv) == 1:
    remove()
else:
    print('please enter folder name')