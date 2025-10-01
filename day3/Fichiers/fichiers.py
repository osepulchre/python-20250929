import os
from collections import Counter
from threading import Thread

def process_file(file_name:str):
        with open(file_path, 'rb') as f:
            contenu=f.read()
            compteur = Counter(contenu)
            print(f"{file_name}: {os.path.getsize(file_path)}: {compteur}")
            f.close()

def process_files():
    try:
        file = files.pop()
        while True:
            process_file(file)
            file=files.pop()
    except IndexError:
        pass

dir_path="d:\\temp\\"

# lister les fichiers
files=[]
for file_name in os.listdir(dir_path):
    file_path=dir_path+file_name
    if os.path.isfile(file_path):
        files.append(file_path)

print(files)

threads=[]
nb_threads=10
for i in range(nb_threads):
    t=Thread(target=process_files)
    threads.append(t)
    t.start()

for i in range(nb_threads):
    t.join()


