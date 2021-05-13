from threading import Thread # this is a thread access object
import time
import random
import sys

# create a runnable class (ie override the Thread run method)
class MyClass(Thread): # Thread has a built in run method
    def __init__(self, name):
        Thread.__init__(self) # call the init method of the parent class
        self.name = name
    def run(self):
        for i in range(1,50):
            time.sleep(random.random()*0.1)
            sys.stdout.write(self.name) # or print()

if __name__ == '__main__':
    m1 = MyClass('m1')
    m2 = MyClass('m2')
    print('begin the threads...')
    m1.start()
    m2.start()
    print('waiting for threads to join...')
    m1.join() # at this moment all the stdout is returned to the main thread
    m2.join()
    print('all done')