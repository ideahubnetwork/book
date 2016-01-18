import multiprocessing
import threading
import time

class Countdown(object):
    def __init__(self):
        self._runing = True

    def terminate(self):
        self._runing = False

    def run(self, n):
        while self._runing and n  > 0:
            print(n)
            n -= 1
            time.sleep(1)

# c = Countdown()
# # 在python3中可以加daemon参数，代表守护线程，无法join，主线程结束自动销毁。
# t = threading.Thread(target=c.run, args=(1000, ))        
# t.start()
# print(t.is_alive())

c = Countdown()
p = multiprocessing.Process(target=c.run, args=(1000,))
p.start()