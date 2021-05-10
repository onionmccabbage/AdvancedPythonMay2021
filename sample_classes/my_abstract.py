# abc is the astract base class
from abc import ABCMeta, abstractmethod, abstractproperty

# we can declare an abstract top-level class
class Shape():
    __metaclass__ = ABCMeta # this is a meta class
    # we can declare abstract methods for this class
    @abstractmethod
    def display(self):
        pass
    @abstractproperty
    def name(self):
        pass # we declare NO body to the method


