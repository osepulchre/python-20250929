from concurrent.futures import ThreadPoolExecutor
import time
import random

def task(num):
    print(f">task {num} started.")
    time.sleep(random.uniform(1,4))
    print(f"<task {num} completed.")
    return f"-> task {num} result"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = list([executor.submit(task,i) for i in range(15)])
    completed_futures=[]

    completed=False
    while not completed:
        time.sleep(0.1)
        completed=True
        for future in futures:
            if future.done():
                if not future in completed_futures:
                    print(future.result())
                    completed_futures.append(future)
            else:
                completed=False
