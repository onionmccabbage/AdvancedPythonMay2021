from threading import Thread, Lock
import time
import random
import sys

counter = 0
lock = Lock()

def workerA():
    global counter
    lock.acquire()
    try:
        while counter <10:
            counter +=1
            print('A increments counter to {}'.format(counter))
            time.sleep(random.randint(0,1))
    except Exception as err:
        print(err)
    finally:
        lock.release()

def workerB():
    global counter
    lock.acquire()
    try:
        while counter >-10:
            counter -=1
            print('B decrements counter to {}'.format(counter))
            time.sleep(random.randint(0,1))
    except Exception as err:
        print(err)
    finally:
        lock.release()

def main():
    start = time.time()
    thread1 = Thread(target=workerA)
    thread2 = Thread(target=workerB)
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
    end = time.time()
    print('Time: {}'.format(end-start))

if __name__ == '__main__':
    main()