from threading import Thread
from Queue import Queue


class WorkerThread(Thread):

    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.input_queue = Queue()

    def send(self, item):
        self.input_queue.put(item)

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()
        print('close....')

    def run(self):
        while True:
            item = self.input_queue.get()
            print('.'*50)
            if item is None:
                break
            print(item)
            self.input_queue.task_done()
        self.input_queue.task_done()
        return

w = WorkerThread()
w.start()
w.send('hello, world')
w.send('hello, tian')
w.close()
