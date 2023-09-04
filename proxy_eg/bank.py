from payment import Payment
import random # this bank will responbd randomly

class Bank(Payment):
    '''This is a bank for making payments'''
    def __init__(self):
        self.card = None
        self.account = None

    def setCard(self, card):
        self.card = card
    def __getAccount(self):
        self.account = self.card
        return self.account
    
    # random amount of funds...
    def __has_funds(self):
        print(f'Bank is checking if {self.__getAccount()} has available funds')
        return bool(random.getrandbits(1))


    def do_pay(self):
        if self.__has_funds():
            print('Bank is paying')
            return True
        else:
            print('Insufficient funds')
            return False