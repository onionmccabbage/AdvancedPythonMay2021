import doctest

# declare some functions that contain documentation tests (doctest)
def nthPower(d,p):
    '''
    This function return a number raised to a power
    >>> nthPower(-3,2)
    9
    >>> nthPower(0,10000)
    0
    >>> nthPower(5,3)
    125
    '''
    return d**p

def square_it(x):
    '''
    return the square of any number less than ten
    >>> square_it(3)
    9
    >>> square_it(16) # we expect an exception
    Traceback (most recent call last):
    ...
    ValueError: input too large
    '''
    if x>9:
        raise ValueError('input too large')
    else:
        return x*x

def cubeIt(a, b):
    '''
    Return the cube of all numbers in range a to b
    >>> cubeIt(1,3)
    [1, 8, 27]
    >>> cubeIt(1,10) # doctest:+ELLIPSIS
    [1, 8, ..., 1000]
    '''
    answers = []
    for i in range(a, b+1):
        answers.append(i*i*i)
    return answers

if __name__ == '__main__':
    # result = nthPower(3,100000)
    # print(result)
    doctest.testmod(verbose=True)