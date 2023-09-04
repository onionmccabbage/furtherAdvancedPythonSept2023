# a facade brings together disparate entities

# here is a bunch of classes
class Coder():
    '''creates code to solve problems'''
    def __init__(self):
        print('write some code')
    def __is_available__(self):
        print('coding skills are available')
        return True # or False
    def book_time(self):
        if self.__is_available__():
            print('coder has been booked')

class Tester():
    '''tests code to ensure diligence'''
    def __init__(self):
        print('preparing some tests')
    def testing(self):
        print('tests are in place')

class Technician():
    '''solve technical issues'''
    def __init__(self):
        print('preparing equipment for the team')
    def doStuff(self):
        print('network, machines, cloud etc all in place')

class Artisan():
    '''design stuff'''
    def __init__(self):
        print('Designing things')
    def make_prototype(self):
        print('Wireframes are ready')

class Manager():
    '''manage the other roles'''

# the above 'manager' facade might be invoked by a client
class Client():
    '''needs to have stuff done'''

if __name__ == '__main__':
    '''a facade can make ugly stuff easier to look at'''