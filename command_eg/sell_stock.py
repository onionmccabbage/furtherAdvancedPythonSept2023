from order import Order

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock # invoke the stock.setter method
    # getter and setter methods
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if new_stock != '':
            self.__stock = new_stock
        else:
            raise Exception('problem with stock name')
    def execute(self):
        return self.stock.sell()


if __name__ == '__main__':
    pass