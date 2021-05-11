# in Python 3 we have a 'context manager'
from contextlib import contextmanager # here we import the contextmanager decorator
import sys

@contextmanager
def stdout_redirect(new_stdout):
    save_stdout = sys.stdout
    sys.stdout = new_stdout
    yield # this function will yield the next available object to be written
    #reset to the default
    sys.stdout = save_stdout

if __name__ == '__main__':
    with open('mylog.txt','a') as fobj:
        with stdout_redirect(fobj):
            print('this is redirected by our decorated method')
    print('and back to the terminal')

