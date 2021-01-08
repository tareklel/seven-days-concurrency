from queue import Queue
from time import sleep
from threading import Thread

_sentinel = object()
queue = Queue()

def producer(out_q, iterations):
    # set number of iterations to put ints in queue
    for x in range(iterations):
        out_q.put(x)
    # place sentinel in queue
    out_q.put(_sentinel)

def consumer(in_q, name):
    while True:
        # get object from queue
        data = in_q.get()
        print(f'object {data} received by {name}')
        sleep(1)
        if data == _sentinel:
            # if sentinel received stop thread
            in_q.put(_sentinel)
            print(f'{name} completed its job')
            break

if __name__=='__main__':
    producer_thread = Thread(target=producer, args=(queue, 20))
    consumer_thread1 = Thread(target=consumer, args=(queue, 'thread 1'))
    consumer_thread2 = Thread(target=consumer, args=(queue, 'thread 2'))
    producer_thread.start()
    consumer_thread1.start()
    consumer_thread2.start()
            
        
