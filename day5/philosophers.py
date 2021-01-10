'''
DAY 5 OF CONCURRENCY: DINING PHILOSOPHERS
'''
from time import sleep
import threading
from contextlib import contextmanager

@contextmanager
def acquire(*locks):
    # sort locks
    locks = sorted(locks, key=lambda x: id(x))
    try:
        for lock in locks:
            lock.acquire() 
        yield
    finally:
        # release locks
        for lock in locks:
            lock.release()

# Thread representing a philosopher
def philosopher(left, right): 
    while True:
        # philosopher can have two 'chopsticks' at a time
        with acquire(left, right): 
            print(f'{threading.currentThread()} is eating')

# locks representing chopsticks 
STICKSNUMBER = 5
chopsticks = [threading.Lock() for n in range(STICKSNUMBER)]

# create all pholsophers
for n in range(STICKSNUMBER):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n], chopsticks[(n+1)%STICKSNUMBER])
                         )
    t.start()
    
