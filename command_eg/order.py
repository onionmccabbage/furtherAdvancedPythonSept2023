from abc import ABCMeta, abstractmethod

# an abstract class
class Order(metaclass=ABCMeta): # inherit from ABC
    @abstractmethod
    def execute(self):
        pass # never implement in abstractions

if __name__ == '__main__':
    pass