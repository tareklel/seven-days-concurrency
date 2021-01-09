'''
DAY 4 OF CONCURRENCY: AVOIDING DEADLOCKS
'''

from time import sleep
import threading
from contextlib import contextmanager

x_lock = threading.Lock() 
y_lock = threading.Lock()

@contextmanager
def acquire(*locks):
    # sort locks
    locks = sorted(locks, key=lambda x: id(x))
    try:
        for lock in locks:
            lock.acquire() 
        yield
    finally:
        # Release locks in reverse order of acquisition 
        for lock in locks:
            lock.release()

def thread(n): 
    while True:
        with acquire(x_lock, y_lock): 
            print(f'thread {n}')


t1 = threading.Thread(target=thread, args=(1,)) 
t1.start()
t2 = threading.Thread(target=thread, args=(2,)) 
t2.start()
