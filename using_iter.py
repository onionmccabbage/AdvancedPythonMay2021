mylist = [1, 7, 11, 42]

# we can create our own iterable from a collection
list_iter = iter(mylist) # this is now our own iterable - not the list iterable
# more iterables
rev_list = reversed(mylist)

print( list_iter.__next__() )
print( list_iter.__next__() )
print( list_iter.__next__() )
print( list_iter.__next__() )
# print( list_iter.__next__() ) # fails - we have exhausted the iterable
print( rev_list.__next__() ) # 42