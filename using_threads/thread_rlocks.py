# rlocks are re-entrant locks. If we need to acquire then release a lock often, 
# it is more performant to use a re-entrant lock
import threading
import time
class MyWorker(): # note - we are not explicitly inheriting from Thread
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock() # this could be a global RLock
    def modifyA(self):
        with self.rlock:
            print(f'RLock acquired {self.rlock._is_owned()} to modify "a"')
            self.a += 1
            time.sleep(1)
    def modifyB(self):
        # using 'with' will release the RLock when it completes
        with self.rlock:
            # _is_owned returns True when the RLock is being used
            print(f'RLock acquired {self.rlock._is_owned()} to modify "b"')
            self.b -= 1
            time.sleep(1)
            # no need to release the RLock, it will be released when the 'with' operator completes
    def modifyBoth(self):
        self.modifyA()
        self.modifyB()

if __name__ == '__main__':
    worker = MyWorker() # NB this is NOT a thread instance
    worker.modifyA() # use the rlock
    worker.modifyB() # use the rlock
    worker.modifyBoth() # use the rlock
