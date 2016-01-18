x = 18
print(eval('x+x'))

# exec('for i in range(100):print(i)')

e = compile('for i in range(100):print(i)', '','exec')
exec(e)