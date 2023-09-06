from threading import Lock

lock = Lock()

# here is a function to be used as a decorator
def lock_a_method(meth):
    '''This can be used to decorate any method that needs to be thread safe'''
    if getattr(meth, '__is_locked', False):
        '''we could do nothing but here we choose to raise and exception'''
        raise TypeError(f'Method {meth} is already locked')
    def locked_method(self, *args, **kwargs):
        try:
            # lock.acquire()
            # result = meth(self, *args, **kwargs)
            # return result
            with lock: # instead of lock.acquire() and release()
                return meth(self, *args, **kwargs)
        except Exception as e:
            print(e)
        # finally:
        #     lock.release()
    lock_a_method.__name__ = f'Locked Method {meth.__name__}'
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, meth_l, lock_factory):
    '''iterate over all the methods in meth_l making each thread safe'''
    init = cls.__init__ # take a copy of the current __init__ method
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock_factory # typically a 'Lock'
    cls.__init__ = new_init # replace the original __init__ method
    for meth in meth_l:
        old_meth = getattr(cls, meth)
        new_meth = lock_a_method(old_meth)
        setattr(cls, meth, new_meth)
    return cls

# here is a function to be used as a decorator to make selected methods of the class thread safe
def lock_a_class(meth_list, lock_factory): # lock_factory is any 'Lock' type
    return lambda cls: make_thread_safe(cls, meth_list, lock_factory)

# here is a class - we will apply our decorator to lock some methods of this class
@lock_a_class(['add', 'remove'], Lock)
class MyClass(set): # here we extend the set type
    def __init__(self, new_set):
        set.__init__(self, new_set) # call the initializer of the 'set' type
    @lock_a_method # apply our decorator to one function
    def someMethod(self):
        '''carry out some operation that might need to be thread safe'''
        print('here is an arbitrary method')

if __name__ == '__main__':
    my_set = {4, 3, 2}
    s = MyClass(my_set)
    # see if 'someMethod' is locked
    s.someMethod() # call the actual method
    print(s.someMethod.__is_locked) # False or error ( it doesn't exist)
    # try out the lock_a_class
    s.add('apples')
    s.remove(2)