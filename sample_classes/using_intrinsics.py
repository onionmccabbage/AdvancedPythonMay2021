# we can acces five intrinsic properties of any class

class TopLevel(): # everything ultimately descends from Object
    def __init__(self):
        pass

class Derived(TopLevel):
    '''
    This class is derived from the TopLevel class
    It has it's own __str__ method
    '''
    def __init__(self):
        super().__init__()
    def __str__(self):
        return ('Derived class instance')

if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(d)
    print('Class Name is: {}\nClass docstring is: {}'.format(Derived.__name__, Derived.__doc__) )
    print('This class in in a module called {}'.format(Derived.__module__))
    print('The class dict is: {}'.format(Derived.__dict__))
    print('The class bases are: {}'.format(Derived.__bases__))if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(d)
    print('Class Name is: {}\nClass docstring is: {}'.format(Derived.__name__, Derived.__doc__) )
    print('This class in in a module called {}'.format(Derived.__module__))
    print('The class dict is: {}'.format(Derived.__dict__))
    print('The class bases are: {}'.format(Derived.__bases__))