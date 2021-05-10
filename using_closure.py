# closure refers to the moments we actually choose to invoke a function
def minions(say):
    def inner():
        return 'Minions say {}'.format(say)
    return inner

if __name__ == '__main__':
    r = minions('Heheeee')
    s = minions('hahaaaaa')
    print(r, s) # they are just function objects
    print(r(), s()) # this is a closure