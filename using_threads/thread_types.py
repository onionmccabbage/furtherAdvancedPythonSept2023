# we can run many threads on one processor
# threads may be classes or functions

from threading import Thread # Thread is a thread-access-object (not an actual Thread)

import time
import random

def someFn(n):
    '''this function will simply sleep for a short time'''
    for i in range(0, 50):
        time.sleep(random.random()*0.1 ) # sleep for up to a tenth of a second
        print(n)





if __name__ == '__main__':
    t1 = Thread(target=someFn, args=('thread 1',)) # Arguments are provided in a tuple
    t2 = Thread(target=someFn, args=('thread 2',)) # Arguments are provided in a tuple
    t3 = Thread(target=someFn, args=('thread 3',)) # Arguments are provided in a tuple
    t4 = Thread(target=someFn, args=('thread 4',)) # Arguments are provided in a tuple
    # we can measure time
    start = time.time()

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # we can make our main thread pause until the other threads are complete
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    end = time.time()
    # careful - the main thread just carries on despite other threads running
    # so we use 'join' to pause the main thread until the other threads re-join the main
    print(f'Total time {end-start}')
