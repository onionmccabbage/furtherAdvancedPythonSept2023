# modern python lets us manage asynchronous code using 'async'
# previously we would use coroutines for this

import asyncio

@asyncio.coroutine
def cube(n):
    '''this needs to be asynchronous (maybe it takes a loooong time)'''
    return n*n*n

# now there is no need to import anything, async is built in to python
async def square(n):
    '''might be a long running function'''
    await( asyncio.sleep(2) ) # we can await any async function
    return n*n

# NB both functions will be threaded (due to async)
if __name__ == '__main__':
    s = asyncio.run(cube(3))
    print(s) #27
    d = asyncio.run(square(2))
    print(d) # 4
