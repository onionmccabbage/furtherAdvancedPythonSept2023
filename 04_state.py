# state is simply the data we pass around
# we may need to react to changes in state
# sometimes state can be represented in classes 
# alternatively we might mutate a stucture which represents our state
# this has become known as "reactive programming"

class ComputerState:
    name='state'
    allowed = []
    def switch(self, state):
        if state.name in self.allowed:
            print(f'Current state {self} switching to {state.name}')
            # we mst remember to implement the state change
            self.__class__ = state
        else:
            print(f'Current state {self} cannot switch to {state.name}')
    def __str__(self):
        return self.name # or any string representation of this class
    
# in this case we have a separate class for each state
class On(ComputerState):
    name='On'
    allowed = ['Off', 'Sleep', 'Hybernate']

class Off(ComputerState):
    name='Off'
    allowed = ['On']

class Sleep(ComputerState):
    name='Sleep'
    allowed = ['On']

class Hybernate(ComputerState):
    name='Hybernate'
    allowed = ['On']

class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.state = Off() # an instance of the 'Off' class
    def change(self, change_to):
        self.state.switch(change_to)

def main():
    c = Computer('Laptop')
    c.change(On)
    c.change(Off)
    c.change(On)
    c.change(Sleep)
    c.change(On)
    c.change(Hybernate)
    c.change(On)
    c.change(Off)
    c.change(Hybernate) # fail
    c.change(Sleep) # fail

if __name__ == '__main__':
    main()