import json

class Item:
    def __init__(self, name, cost):
        self.name = name # these call the setter methods below
        self.cost = cost
    def __str__(self): # how to print thsi class
        return 'Name: {} Cost: {}'.format(self.name, self.cost) # here we use the accessor methods
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost):
        self.__cost = cost

# here is a class which will encode our item class
class ItemEncoder(json.JSONEncoder):
    def default(self, obj): # override the default encoder method
        if isinstance(obj, Item):
            return obj.__dict__
        # if type is wrong, pass to base class (JSONEncoder) which raises an exception
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    laptop = Item('laptop', 850)
    itemJSON = json.dumps(laptop, cls=ItemEncoder) # uses our override encoder
    print(itemJSON, type(itemJSON))