from threading import Thread, Lock
import time
import random
import sys

def main():
    lock = Lock() # create an instance of a lock
    # acquire a lock - remember to release it too!
    lock.acquire()
    try:
        for i in range(1,50): # a long running process - e.g. external access
                time.sleep(random.random()*0.1)
                sys.stdout.write('{} '.format(i))
    except Exception as err:
        pass
    finally:   
        lock.release() # make sure we release the lock!!

    # alternative syntax
    with lock: # here we recycle the lock
        for i in range(1,50): # a long running process - e.g. external access
                time.sleep(random.random()*0.1)
                sys.stdout.write('{} '.format(i))
    # no need to release the lock, it is automatically released when the with ends

if __name__ == '__main__':
    main()