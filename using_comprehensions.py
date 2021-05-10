# note - all this code is in the global name-space
# we can comprehensively iterate over a collection by using comprehensions
l = [5,4,3,2,1]
# here we have a list comprehension
# [ expression for item in iterable ]
my_numbers = [n*n for n in l]
print(my_numbers)
my_others = [n*n for n in range(5,0,-1)]
print(my_others)
# NB range is an iterable generator
r = range(-99,100)
print(r)
# dictionary comprehension
# { key_expression : value_expression for expression in iterable}
word = 'letters' # a string (a collection of characters)
letter_counts = { letter:word.count(letter) for letter in word }
print(letter_counts)

# set comprehension - say we want a set of values which are multiples of three
my_set = { number for number in range(-9,10) if number%3 == 0 }
print(my_set)

# now we define some functions (which have their own namespace)
# we can declare our OWN generator objects
def my_range(first=0, last=10*100, step=1):
    number = first
    while number < last:
        # instead of a return statement we have a yield statement
        yield number # yields the next value in the sequence being generated
        number +=step

if __name__ == '__main__':
    inst = my_range(3, 9, 2)
    # lets see what sort of object we have
    print(inst)
    # my_range(last=3, first=9, step=-2)
    # we can use our generator to iterate
    for item in inst:
        print(item)

    # we can explicitly call the net items in the generator
    inst2 = my_range()
    print( inst2.__next__() ) # yields 0
    print( inst2.__next__() ) # yields 1
    print( inst2.__next__() ) # yields 2
    print( inst2.__next__() ) # yields 3
    # we can access the nect member any time we like
    print('{}, {}, {}'.format(inst2.__next__(), inst2.__next__(), inst2.__next__()))

    # we have exhauseted inst, so there's nothing left to yield
    # print(inst.__next__()) 