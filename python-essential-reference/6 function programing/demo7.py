def start(func):
    def _start(*arg, **kwargs):
        g = func(*arg, **kwargs)
        g.next()
        return g
    return _start

@start
def receiver():
    print('Ready to receive')
    result = None
    while True:
        result = (yield )
        print('get', result)

r = receiver()
a = r.send(12)
print(a)