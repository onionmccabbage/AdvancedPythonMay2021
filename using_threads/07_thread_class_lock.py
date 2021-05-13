from threading import Thread, Lock

lock = Lock()
count1 = 0
count2 = 0

class MyClass:
    def __call__(self, name):
        global lock, count1, count2
        # iterate to handle count1
        for i in range(0, 20): # adjust this
            count1 += 1
            print('c1: {}'.format(count1))
            
        # iterate to handle count2 with a lock
        lock.acquire()
        for i in range(0, 20): # adjust this
            count2 += 1
            print('c2: {}'.format(count2))
        lock.release()

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('t1',))
    t2 = Thread(target=m1, args=('t2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(count1, count2)