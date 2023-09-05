# semaphores let us specify the maximum number of concurrent threads
# this will depend on resources 
import random
import time
import threading

# a global asset
ticketsAvailable = 100

class TicketSeller(threading.Thread): # we inherit fro mthe Thread class
    '''use a semaphore to access the tickets sold'''
    ticketsSold = 0
    def __init__(self, sem): # pass in a semaphore
        threading.Thread.__init__(self)
        self.__sem = sem
    def run(self):
        global ticketsAvailable
        running=True
        while running:
            self.__sem.acquire() # get access to the semaphore
            self.randomDelay() # randomly sleep
            if ticketsAvailable <= 0:
                running=False
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
            self.__sem.release() # release the semaphore
    def randomDelay(self):
        time.sleep(random.randint(0,4)/16) # 0, 0.25, 0.5 or 0.75 seconds


def main():
    ''' provide a semaphore then a number of ticket seller instances'''
    sem = threading.Semaphore()
    sellers = []
    for i in range(0, 16):
        seller = TicketSeller(sem) # pass the global semaphore to our instance
        sellers.append(seller)
        seller.start()
    # once all the threads have started, we can call 'join'
    for seller in sellers:
        seller.join()

if __name__ == '__main__':
    main()

