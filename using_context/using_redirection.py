# we can write a class to redirect the context (simple solution)
import sys # sys is in control of inputs and outputs

class Redirect:
    '''
    Provide an easy way to redirect the standard output
    (which defaults to printing to the console)
    '''
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
    # we override __enter__ and __exit__
    def __enter__(self):
        '''implement a redirection'''
        #store the current stdout
        self.save_stdout = sys.stdout
        #set a new stdout
        sys.stdout = self.new_stdout # we have redefined a member of sys!!!!
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''restore the original stdout'''
        sys.stdout = self.save_stdout

if __name__ == '__main__':
    # print(sys.stdout)
    # make use of our redicetion class
    with open('mylog.txt', 'a') as fobj: # open a file access object
        with Redirect(fobj):
            print('this gets printed to our log file') # look - no file reference
    print('this will print to the console') # back to stdout default

