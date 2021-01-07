import threading
import time
import random

def worker(n, sema):
    # Wait to be signaled 
    sema.acquire()
    # wait for other tasks to finish
    time.sleep(random.randint(0,2))
    # Do some work
    global total
    total += n
    print('Working', total)
    # release semaphore
    sema.release()

# Create some threads
sema = threading.Semaphore() 
nworkers = 5
total = 0
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,)) 
    t.start()

