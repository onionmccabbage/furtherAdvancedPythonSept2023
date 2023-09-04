from payment import Payment
from bank import Bank

class DebitCard(Payment):
    '''The debit card is a proxy for the bank'''
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card=input('Swipe, tap, insert or zap? ')
        self.bank.setCard(card)
        # there should be TONS of authentication and validation here...
        return self.bank.do_pay() # True or False