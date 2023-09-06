from memory_profiler import profile
import collections # a bunch of additional data structures

@profile # invoke the built-in memory profiler
def someFn():
    '''manage a double-ended queue (mutable collection of any data types)'''
    my_deq = collections.deque('98765432')
    print(f'Deque: {my_deq}')
    my_deq.append('1')
    print(f'Deque: {my_deq}')
    my_deq.appendleft('0')
    print(f'Deque: {my_deq}')
    my_deq.pop() # remove the right-most member
    my_deq.popleft() # remove the left-most member
    print(f'Deque: {my_deq}')
    # we can consume a lot of system memory
    for i in range(0, 1024**3):
        my_deq.append( str(i) )


if __name__ == '__main__':
    someFn()