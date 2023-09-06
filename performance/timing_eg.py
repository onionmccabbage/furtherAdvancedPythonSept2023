from time import time
from timeit import default_timer # this is a more accurate tool
from functools import reduce

def fib(n):
    '''fibonacci is a sequence of mathematics to endlessly return a pattern of numbers
    1, 2, 3, 5, 8, 13, 21 '''
    if n<=1:
        return 1
    else:
        # iteratively call the same function
        return ( fib(n-1)+fib(n-2) )

def fib2(n):
    '''a more performant solution'''
    sequence = (0,1)
    for _ in range(2, n+2): # remember we need to return the sum of the last TWO members
        '''repeatedly add the last two values of the sequence'''
        # NB here we have a one-member tuple (so remember the trailing comma)
        sequence += (reduce( lambda a,b: a+b, sequence[-2:] ),) # works for a tuple
    # we must return
    return sequence[-1] # the last member

if __name__ == '__main__':
    # n=32 # about 1.5 sec on my laptop
    # n=34 # about 10 sec on my laptop
    n=10000
    # start = time()
    start2 = default_timer()
    for _ in range(2, n+1):
        r = fib2(_)
        # print(r) # remember 'print' is an expensive thing to do
    # end=time()
    end2 = default_timer()
    # print(f'Calculation of {r} took {end-start} seconds')
    print(f'Calculation of {r} took {end2-start2} seconds')
