from threading import Thread, Event
import time
from typing import Any

# we can use events to communicate from Threads
event = Event()

class MyClass:
    def __call__(self, n):
        global event
        print(f'{n} waiting for event...')
        event.wait()
        print(f'{n} continuing after event')

if __name__ == '__main__':
    m1 = MyClass()
    t1 = Thread(target=m1, args=("A", ))
    t1.start()

    # wait on the main thread
    time.sleep(4)
    event.set()
