import threading
import queue
import time

class Job:
    def __init__(self, name, duration):
        self.__duration = duration
        self.name = name

    def perform(self):
        time.sleep(self.__duration)

    def __repr__(self):
        return f"{self.name} ({self.__duration} heures)"

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.__name = name
    
    def run(self):
        try:
            while True:
                job = self.__job_queue.get(timeout=1)
                print(f"{self}: début {job}")
                job.perform()
                print(f"{self}: fin {job}")
                self.__job_queue.task_done()
        except queue.Empty:
            print(f"{self}: fin de la journée")

    def start(self, job_queue):
        self.__job_queue = job_queue
        super().start()
    
    def __repr__(self):
        return self.__name

job_queue = queue.Queue()
for job in [Job("repassage", 2), Job("vaisselle", 1), Job("cuisine", 2), Job("ménage", 3), Job("jardinage", 4), Job("courses", 2), Job("factures", 1), Job("lavage voiture", 1), Job("tonte gazon", 5)]:
    job_queue.put(job)

workers = [Worker("Marge"), Worker("Omer"), Worker("Bart"), Worker("Lisa"), Worker("Maggie")]

for worker in workers:
    worker.start(job_queue)

for worker in workers:
    worker.join()
