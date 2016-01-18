def countdown(n):
    def next():
        nonlocal n
        n -= 1
        return n
    return next


next = countdown(10)
while True:
    v = next()
    print(v)
    if not v:
        break