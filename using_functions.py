# the arguments passed in to a function can be positional or keyword arguments
def myFn(*args): # *args will take all the positional arguments and put them in a tuple
    print(args)
    # no-argument outcome
    if (len(args)==0):
        x=3
        y=4
    # one-argument outcome
    if (len(args)==1):
        x = args[0]
        y=4
    # two or more argument outcome
    if (len(args)>1):
        x = args[0]
        y = args[1]
    return (x*x+y*y)**0.5

def otherFn(*args, **kwargs): # **kwargs will gather all the keyword arguments into a dict
    print(args, kwargs)

if __name__ == '__main__':
    r = myFn(3, 4)
    print(r)
    print(myFn())
    print(myFn(3))
    print(myFn(-3, -4,-5, True))
    #
    otherFn('hello', True, n='hello', x=99, r=myFn(-6,-8) ) # positional args must come before keyword args