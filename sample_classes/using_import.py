from using_intrinsics import Derived

if __name__ == '__main__':
    d = Derived()
    # print(d)
    # print('Class Name is: {}\nClass docstring is: {}'.format(Derived.__name__, Derived.__doc__) )
    # print('This class in in a module called {}'.format(Derived.__module__))
    # print('The class dict is: {}'.format(Derived.__dict__))
    # print('The class bases are: {}'.format(Derived.__bases__))

    # there are also two intrinsic attributes
    d.color = 'Red'
    print(d.__class__)
    print(d.__dict__)