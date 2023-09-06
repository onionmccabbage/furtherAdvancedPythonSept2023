from threading import Lock

lock = Lock()

# here is a function to be used as a decorator
def lock_a_method(meth):
    '''This can be used to decorate any method that needs to be thread safe'''
    if getattr(meth, '__is_locked', False):
        '''we could do nothing but here we choose to raise and exception'''
        raise TypeError(f'Method {meth} is already locked')
    def locked_method(self, *args, **kwargs):
        # NB we cannot use the 'with' operator here
        lock.acquire()
        result = meth(self, *args, **kwargs)
        lock.release()
        return result
    lock_a_method.__name__ = f'Locked Method {meth.__name__}'
    locked_method.__is_locked = True
    return locked_method

# here is a class - we will apply our decorator to lock some methods of this class
