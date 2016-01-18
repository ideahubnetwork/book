import time
import itertools
import threading

def countdown(n):
    for i in itertools.count(n, -1):
        if i == 0:
            break
        print(i)
        time.sleep(1)

t = threading.Thread(target=countdown, args=(3,), daemon=True)
t.start()
t.join()
print('hello, world')