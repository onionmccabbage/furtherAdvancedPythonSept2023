# decorators add something to what we already have

# here is a decorator function
def showArgs(f): # 'f' will be any other function pased in to this one
    '''This will be a decorator for other function
       Reveal all the positional arguments
       and all the keyword arguments
       passed in to any other function'''
    # we can write logging, validate values etc.
    def newFunc(*args, **kwargs):
        print(f'Running a function called {f.__name__}')
        print(f'Positional arguments are {args}') # args is a tuple of any positional aruments
        print(f'Keyword arguments are {kwargs}')  # kwargs is a dictionary of any keyword arguments
        return f(*args, **kwargs)
    return newFunc

# here are some very simple functions
@showArgs # this is how we implement a decorator
def addIntegers(a, b):
    return int(a) + int(b)

@showArgs
def raiseToPower(m, n):
    return m**n

if __name__ == '__main__':
    print( addIntegers(1, 2) )  # 3
    print( addIntegers(1, b=2) )  # 3
    print( addIntegers(a=1, b=2) )  # 3
    print( raiseToPower(10, 2) )  # 100
    print( raiseToPower(10, n=2) )  # 100
    print( raiseToPower(m=10, n=2) )  # 100