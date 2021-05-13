from threading import Thread, Event
import time

event = Event() # a thread event instance

# declare a class which has a thread event
class MyClass:
    def __call__(self, name):
        global event
        print('{} is waiting for event'.format(name))
        event.wait()
        print('{} continuing after the event'.format(name))

if __name__ == '__main__':
    m1 = MyClass()
    t1 = Thread(target=m1, kwargs={'name':'t1'})
    t1. start()
    time.sleep(5)
    # now we can trigger our event
    event.set()
    t1.join()