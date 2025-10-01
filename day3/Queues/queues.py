import random
import queue
import time
from threading import Thread

class Producteur:
    def __init__(self, queue):
        self.__queue = queue
        self.__running = False
        self.__thread = None
    
    def __produire(self):
        value = int(random.uniform(0, 100))
        self.__queue.put(value)
        print(f"posted: {value}")

    def __internal_run(self):
        self.__running = True
        while self.__running:
            self.__produire()
            time.sleep(random.uniform(0,2))

    def __enter__(self):
        self.__thread=Thread(target=self.__internal_run)
        self.__thread.start()
    
    def __exit__(self, type, value, traceback):
        self.__running = False
        self.__queue.put(-1)
        self.__thread.join()
    
class Consommateur:
    def __init__(self, queue):
        self.__queue = queue
        self.__thread = None
        self.__running = False
    
    def __consommer(self):
        value = self.__queue.get()
        if value == -1:
            self.__running=False
        else:
            print(f"read: {value}")
    
    def __internal_run(self):
        self.__running = True
        while self.__running:
            self.__consommer()
            time.sleep(random.uniform(0,3))

    def __enter__(self):
        self.__thread=Thread(target=self.__internal_run)
        self.__thread.start()

    def __exit__(self, type, value, traceback):
        self.__thread.join()


fifo=queue.SimpleQueue()

with Consommateur(fifo):
    with Producteur(fifo):
        time.sleep(15)

