class Duck():
    # property of the class (not of any instance)
    count = 0
    # method of the class (not of any instance)
    @classmethod
    def how_many(cls):
        print('Duck class has {} instances'.format(cls.count))
    def __init__(self, name):
        self.name = name
        Duck.count += 1 # increment the CLASS property
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n # we should check it is valid....
    # the built-in __str__ method is used by print()
    def __str__(self):
        return 'Duck instance name is {}'.format(self.name)

if __name__ == '__main__':
    d1 = Duck('Donald')
    d2 = Duck('Mallard')
    d1.name = 'Howard'
    print(d1) # this will use our __str__ method

    print(Duck.count)
    Duck.how_many()