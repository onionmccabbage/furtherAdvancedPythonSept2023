# a daemon thread will continue to run until the main thread terminates
from threading import Thread
import time

def standardThread():
    print('starting standard thread')
    time.sleep(5)
    print('ending standard thread')

def daemonThread():
    while True: # careful - this is an endless loop!!
        print('heartbeat...')
        time.sleep(0.5)

if __name__ == '__main__':
    s = Thread(target=standardThread)
    d = Thread(target=daemonThread)
    d.setDaemon(True) # we now have a daemon thread
    s.start()
    d.start()
    s.join()
    # if the main thread ends, we have no need ot wait for hte daemon to end, so AVOID join
    # d.join() # we need to manually end the main thread then the daemon thread also terminates