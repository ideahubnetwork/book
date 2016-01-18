from threading import Thread
import multiprocessing
import time

class Countdown(Thread):
    def __init__(self, n):
        # super().__init__()
        super(Countdown, self).__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print(self.n)
            time.sleep(1)
            self.n -= 1


c = Countdown(100)
p = multiprocessing.Process(target=c.run)
p.start()