import multiprocessing
import os
import time

def whichProc():
    '''declare which process this is running on'''
    # time.sleep(3)
    print(f'Running on process {os.getpid()}')


if __name__ == '__main__':
    '''invoke the function into several processes'''
    procs = []
    # remember - processes do not correlate to procesors
    for n in range(0, 128):
        p = multiprocessing.Process(target=whichProc)
        procs.append(p)
        p.start()
    for p in procs: # h main thread to pause until the other processes have completed
        ''''''
    # what about the main process?
    whichProc()