class Point():
    points = 0 # a static property of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.points += 1
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) == int:
            self.__x = new_x
        else:
            raise TypeError
    def moveBy(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def display(self):
        return (self.x, self.y)
    def hypot(self):
        h = (self.x**2+self.y**2)**0.5
        return h

if __name__ == '__main__':
    pass
