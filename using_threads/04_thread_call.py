from threading import Thread # this is a thread access object
import time
import random
import sys

# create a callable class
class MyClass: # NB this is NOT a Thread
    def __call__(self, name):
        for i in range(1,50):
            time.sleep(random.random()*0.1)
            sys.stdout.write(name)


if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    # call our callable class
    t1 = Thread(target=m1, args=('t1',))
    t2 = Thread(target=m1, args=('t2',))
    #start
    t1.start()
    t2.start()
    #join
    t1.join()
    t2.join()