import os
import os.path
import glob

path = os.getcwd()
def search_folder(path):
    for prefix, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pyc'):
                file = os.path.join(prefix, file) 
                print file
                os.remove(file)

search_folder('.')