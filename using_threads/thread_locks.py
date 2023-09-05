import threading

# here is a global asset
counter = 0

# here is a lock for use by all the threads
lock = threading.Lock()

def workerA():
    '''this function will access the global counter'''
    global counter
    lock.acquire()
    try:
        while counter <20:
            counter += 1
            print(f'worker A increments counter to {counter}')
    except Exception as e:
        print(e)
    finally:
        lock.release()

def workerB():
    '''this function will access the global counter'''
    global counter
    lock.acquire()
    try:
        while counter >-20:
            counter -= 1
            print(f'worker B decrements counter to {counter}')
    except Exception as e:
        print(e)
    finally:
        lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)

    t1.start()
    t2.start()

    t1.join()
    t2.join()