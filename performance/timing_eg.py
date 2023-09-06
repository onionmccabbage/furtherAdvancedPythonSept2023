from time import time

def fib(n):
    '''fibonacci is a sequence of mathematics to endlessly return a pattern of numbers
    1, 2, 3, 5, 8, 13, 21 '''
    if n<=1:
        return 1
    else:
        # iteratively call the same function
        return ( fib(n-1)+fib(n-2) )

if __name__ == '__main__':
    n=36
    start = time()
    for _ in range(2, n+1):
        r = fib(_)
        # print(r) # remember 'print' is an expensive thing to do
    end=time()
    print(f'Calculation of {r} took {end-start} seconds')
