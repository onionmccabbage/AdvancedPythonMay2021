# functional programming is fashionable - ecourages encapsulation
from functools import reduce # not part of python

def square(x):
    return x*x
def add(x,y):
    return x+y
def isOdd(x):
    return x%2 != 0 # the filter function must return True or False

if __name__ == '__main__':
    sq_l = list(map( square, range(1,6) )) # take each member of the range and apply the square function
    print(sq_l)

    odds = list(filter(isOdd, range(0,10)))
    print(odds)

    # reduce members from two separate collections by applying a function
    r = reduce( add, odds, 10)
    print(r)