import fileinput 

with fileinput.input('test.txt') as f_input:
    for line in f_input:
        print(f_input.filename(), f_input.lineno(), line, end='')