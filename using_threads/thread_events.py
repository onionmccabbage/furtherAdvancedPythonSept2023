from threading import Thread, Event
import time

class MyClass:
    def __call__(self, name):
        global event
        print(name + " waiting for event...")
        event.wait()
        print('\t' + name + " continue after event.")


if __name__ == '__main__':
    event = Event() # create an event instance
    m1 = MyClass()
    t1 = Thread(target=m1, args=("1",))
    t1.start()

    #wait
    time.sleep(5)
    event.set()