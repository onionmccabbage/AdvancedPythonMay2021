# we can override any of the built in operators

# we can write a class with an __eq__ method for equality
class Word():
    def __init__(self, text):
        self.text = text
    # here we override the built in equality operator
    def __eq__(self, other_word):
        return self.text.lower() == other_word.text.lower()
    # we can override the __add__ method to place a hyphen between the concatenated words
    def __add__(self, other_word):
        return '{}-{}'.format(self.text, other_word.text)

# Magic methods for comparison
# __eq__( self, other ) self == other
# __ne__( self, other ) self != other
# __lt__( self, other ) self < other
# __gt__( self, other ) self > other
# __le__( self, other ) self <= other
# __ge__( self, other ) self >= other
# Magic methods for math
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other


if __name__ == '__main__':
    str1 = 'Ha'
    str2 = 'ha'
    print(str1 == str2) # False

    w1 = Word('Ha')
    w2 = Word('ha')
    print(w1 == w2) # True - uses our __str__ method
    print(w1+w2)