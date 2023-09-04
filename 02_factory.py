# the factory pattern lets us manufacture required entities

# abc is abstract base class
from abc import abstractmethod

# here is a top-level abstract class
class Animal():
    '''All our creatures will inherit from this abstract class'''
    @abstractmethod
    def make_a_noise(self):
        pass # never implement features in abstract

# here are some concrete classes (usually in a separate module)
class Dog(Animal):
    def make_a_noise(self):
        print('woof')
class Cat(Animal):
    def make_a_noise(self):
        print('miaow')
class Lion(Animal):
    def make_a_noise(self):
        print('roar')
class Bat(Animal):
    def make_a_noise(self):
        print('______')

# here is a factory to create our animals
class CreatureFactory():
    '''this is a single-point-of-access for all our creatues'''
    def make_sound(self, obj):
        return eval(obj)().make_a_noise()

if __name__ == '__main__':
    cf = CreatureFactory() # we now have an instance of our creature factory
    creature = input('which creature? ') # we ought to validate...
    # use ourfactory to return the creartue capability
    cf.make_sound(creature)





