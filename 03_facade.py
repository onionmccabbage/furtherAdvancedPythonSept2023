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
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        # The facade will provide instances of all the subsystems/microservices needed
        self.coder      = Coder()
        self.tester     = Tester()
        self.technician = Technician()
        self.artisan    = Artisan()
        # put them to work (we could pass arguments)
        self.coder.book_time()
        self.tester.testing()
        self.technician.doStuff()
        self.artisan.make_prototype()

 # the above 'manager' facade might be invoked by a client
class Client():
    '''needs to have stuff done'''
    def __init__(self):
        print('We need a project team')
    def askManager(self):
        print('lets talk to the manager')
        self.manager = Manager()
        self.manager.arrange()
    def __del__(self): # every class in Python will run __del__ when it finishes
        print('all done')

if __name__ == '__main__':
    '''a facade can make ugly stuff easier to look at'''
    customer = Client()
    customer.askManager()