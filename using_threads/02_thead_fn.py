# threads are parallelism within a process
from threading import Thread # this is a thread access object
import time
import random
import sys


def myFunc(name):
    for i in range(1,50):
        time.sleep(random.random()*0.1)
        sys.stdout.write(name) # or print()

if __name__ == '__main__':
    # call our function as Threads
    thread1 = Thread(target=myFunc, args=('t1',)) # arguments are passed as a tuple
    thread2 = Thread(target=myFunc, kwargs={'name':'t2'}) # arguments are passed as a tuple
    # we need to start our threads
    thread1.start()
    thread2.start()
    # when the threads have completed, we can rejoim the main thread
    print('waiting for the threaads to join...\n')
    thread1.join()
    thread2.join()
    print('all done') # the main thread is blocked until the other threads complete