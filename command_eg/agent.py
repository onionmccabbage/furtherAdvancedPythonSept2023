class Agent():
    ''' the agent can issue commands (things to be done)'''
    def __init__(self):
        self.__orderQueue = [] # start with an empty array
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

if __name__ == '__main__':
    pass