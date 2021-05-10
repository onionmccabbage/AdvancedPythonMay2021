
# declare a decorator function
def show_args(func):
    def new_function(*args, **kwargs):
        print('Running function {}'.format(func.__name__))
        print('Positional arguments: {}'.format(args))
        print('keyword arguments: {}'.format(kwargs))
        result = func(*args, **kwargs)
        return result
    return new_function

# declare a basic utility function
@show_args
def add_ints(a, b):
    return a+b

@show_args
def sub_ints(a, b):
    return a-b

# immediate code
if __name__ == '__main__':
   a = add_ints(3, 7)
   print(a)
   b = sub_ints(7, 3)
   print(b)
   c = add_ints(a=3, b=9)
   d = sub_ints(6, b=2)
   print(c, d)