import multiprocessing
import os
import time

# Process is a Process access object (not a Process itself)
class MyProc(multiprocessing.Process):
    def __init__(self):
        super(MyProc, self).__init__()
    def run(self):
        time.sleep(2)
        print(f'Child process ID is {multiprocessing.current_process().pid}')

def main():
    procs_l = []
    for n in range(os.cpu_count()):
        ''' start new processes with their own process ID'''
        '''reminder: each process will have its own copy of python'''
        p = MyProc()
        procs_l.append(p)
        p.start() # this invokes the 'run' method
    for p in procs_l:
        p.join() # this is optional

if __name__ == '__main__':
    main()