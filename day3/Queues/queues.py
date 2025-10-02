import random
import queue
import time
from threading import Thread

class Producteur(Thread):
    def __init__(self, queue):
        super().__init__()
        self.__queue = queue
        self.__running = False
    
    def __produire(self):
        value = int(random.uniform(0, 100))
        self.__queue.put(value)
        print(f"posted: {value}")

    def run(self):
        self.__running = True
        while self.__running:
            self.__produire()
            time.sleep(random.uniform(0,2))

    def __enter__(self):
        self.start()
    
    def __exit__(self, type, value, traceback):
        self.__running = False
        self.__queue.put(-1)
        self.join()
    
class Consommateur(Thread):
    def __init__(self, queue):
        super().__init__()
        self.__queue = queue
        self.__running = False
    
    def __consommer(self):
        value = self.__queue.get()
        if value == -1:
            self.__running=False
        else:
            print(f"read: {value}")
        self.__queue.task_done()
    
    def run(self):
        self.__running = True
        while self.__running:
            self.__consommer()
            time.sleep(random.uniform(0,3))

    def __enter__(self):
        self.start()

    def __exit__(self, type, value, traceback):
        self.join()


fifo=queue.Queue()

with Consommateur(fifo):
    with Producteur(fifo):
        time.sleep(15)


