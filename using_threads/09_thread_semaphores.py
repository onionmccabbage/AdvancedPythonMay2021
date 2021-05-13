from threading import Thread, BoundedSemaphore, Lock
import time

# declare a global semaphore
semaphore = BoundedSemaphore(2) # we can say how many can share this semaphore

class MyClass:
    def __call__(self, name):
        global semaphore
        semaphore.acquire()
        time.sleep(3)
        semaphore.release()


def main():
    m1 = MyClass()
    m2 = MyClass()
    m3 = MyClass()
    m4 = MyClass()
    m5 = MyClass()
    m6 = MyClass()
    start = time.time()
    t1 = Thread(target=m1, args=('t1',))
    t2 = Thread(target=m1, args=('t2',))
    t3 = Thread(target=m1, args=('t3',))
    t4 = Thread(target=m1, args=('t4',))
    t5 = Thread(target=m1, args=('t5',))
    t6 = Thread(target=m1, args=('t6',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    # this semaphore allows 2 at a time. So 2 run for 3 sec then 2 more run 3 sec and the last 2 for 3 sec
    # total estimate about 9 seconds

    end = time.time()
    print('It took {} seconds'.format(end-start))

if __name__ == '__main__':
    main()
