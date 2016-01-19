def foo():
    for n in xrange(5):
        print('i am foo {}'.format(n))
        yield n


def bar():
    for n in xrange(8):
        print('i am bar {}'.format(n))
        yield n


def spam():
    for n in xrange(10):
        print('i am spam {}'.format(n))
        yield n


from collections import deque
taskqueue = deque()
taskqueue.append(foo())
taskqueue.append(bar())
taskqueue.append(spam())

while taskqueue:
    task = taskqueue.pop()
    try:
        item = next(task)
        print(item)
        taskqueue.appendleft(task)
    except StopIteration:
        pass
