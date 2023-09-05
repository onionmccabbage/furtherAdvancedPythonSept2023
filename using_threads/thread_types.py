# we can run many threads on one processor
# threads may be classes or functions

from collections.abc import Callable, Iterable, Mapping
from threading import Thread # Thread is a thread-access-object (not an actual Thread)

import time
import random
from typing import Any

def someFn(n):
    '''this function will simply sleep for a short time'''
    for i in range(0, 50):
        time.sleep(random.random()*0.1 ) # sleep for up to a tenth of a second
        print(n)

class SomeClass(Thread):
    def __init__(self, n ):
        # super().__init__(self, )
        Thread.__init__(self) # call the __init__ of the parent class including Thread defaults
        # self.n = n
    # the Thread class has a 'run' method which we can override
    def run(self):
        for i in range(0, 50):
            time.sleep(random.random()*0.1 ) # sleep for up to a tenth of a second
            print(self.n)


if __name__ == '__main__':
    t1 = Thread(target=someFn, args=('thread 1',)) # Arguments are provided in a tuple
    t2 = Thread(target=someFn, args=('thread 2',)) # Arguments are provided in a tuple
    t3 = Thread(target=someFn, args=('thread 3',)) # Arguments are provided in a tuple
    t4 = Thread(target=someFn, args=('thread 4',)) # Arguments are provided in a tuple
    
    tA = SomeClass('thread A')
    tB = SomeClass('thread B')
    tC = SomeClass('thread C')
    tD = SomeClass('thread D')
    
    # we can measure time
    start = time.time()

    tA.start()
    tB.start()
    tC.start()
    tD.start()

    # we can make our main thread pause until the other threads are complete
    tA.join()
    tB.join()
    tC.join()
    tD.join()

    end = time.time()
    # careful - the main thread just carries on despite other threads running
    # so we use 'join' to pause the main thread until the other threads re-join the main
    print(f'Total time {end-start}')
