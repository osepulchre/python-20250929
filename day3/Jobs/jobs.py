import threading
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
                job = self.__jobs.pop(0)
                print(f"{self}: début {job}")
                job.perform()
                print(f"{self}: fin {job}")
        except IndexError:
            print(f"{self}: fin de la journée")

    def start(self, jobs):
        self.__jobs = jobs
        super().start()
    
    def __repr__(self):
        return self.__name

jobs = [Job("repassage", 2), Job("vaisselle", 1), Job("cuisine", 2), Job("ménage", 3), Job("jardinage", 4), Job("courses", 2), Job("factures", 1), Job("lavage voiture", 1), Job("tonte gazon", 5)]

workers = [Worker("Marge"), Worker("Omer"), Worker("Bart"), Worker("Lisa"), Worker("Maggie")]

for worker in workers:
    worker.start(jobs)

for worker in workers:
    worker.join()
