from my_abstract import Shape

class Circle(Shape):
    def __init__(self, name):
        self.name = name # use the setter method
    def display(self):
        print('Circle {}'.format(self.__name))
    @property # accessor
    def name(self):
        return self.__name
    @name.setter # mutator
    def name(self, new_name):
        # check name is a non-empty string
        if type(new_name) == str and new_name != '':
            self.__name = new_name
        else:
            self.__name = 'default'


if __name__ == '__main__':
    c = Circle('my_circle')
    c.display()
    print(c.name) # calls the @property method
    c.name = 'changed' # calls the @name.setter method
    c.name = True # uses the default
    c.display()