def countdown(start):
    n = start
    def display():
        print(n)
    def decrement():
        nonlocal n
        n -= 1
    while n > 0:
        display()
        decrement()

i = 10
def foo():
    print(i)

foo()

countdown(100)