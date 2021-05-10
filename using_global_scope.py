# variables live inside a name-space (scope) such as a function
# functions can live inside classes
# classes can live inside modules
# modules can live inside packages
# packages make up a project


# we aim to avoid poluting the global scope
g = 'in the global scope'

def fn():
    global g # we will be referring to the g in the global scope
    g = 'in a local scope'
    print(g)

if __name__ == '__main__':
    print(g)
    fn()
    print(g)