from threading import Thread, RLock, Condition # RLock is a re-entrant lock
import time

# some globals
lock = RLock()
data_available = Condition(lock)

# a class representing a notional stack
class Stack():
    def __init__(self):
        self.data = [] # our stack of data members
    def push(self, item):
        with lock:
            self.data.append(item)
    def pop(self):
        with lock:
            item = self.data.pop()
        return item

# we need a producer and a consumer
def producer():
    for n in range(1,5):
        data_available.acquire() # acquire our re-entrant lock via a condition
        stack.push(n)
        data_available.notify_all()
        data_available.release()
        time.sleep(0.2)

def consumer():
    while True:
        data_available.acquire()
        data_available.wait()
        data = stack.pop()
        data_available.release()
        print('acquired data: {}'.format(data))
        if data == 4:
            break

def main():
    prod_thread = Thread(target=producer)
    cons_thread = Thread(target=consumer)
    prod_thread.start()
    cons_thread.start()
    prod_thread.join()
    cons_thread.join()
    print('all done')

if __name__ == '__main__':
    stack = Stack()
    main()