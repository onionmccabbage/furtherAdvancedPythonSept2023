# a generator is efficient because it's values never persist in memory
for i in range(32):
    print(i) # all the values of 'i' are NOT persisted - this is good

# python will create a generator for us if we need one
even_g = ( i for i in range(100) if i%2==0 ) # not a tuple
print(type(even_g)) # it is a generator
# a generator can yield values
print( even_g.__next__() ) # 0
print( even_g.__next__() ) # 2
print( even_g.__next__() ) # 4
print( even_g.__next__() ) # 6
# we can iterate over a generator
for _ in even_g:
    print(_, end=', ')

# at this point the generator is exhausted
# print( even_g.__next__() ) # nope

# we can build a custom generator
def tally(incr=1):
    ''' keep an endless tally of count'''
    score=0
    while True: # careful
        yield score
        score += incr

game = tally(5) # score increments by 5
print(type(game)) # generator
print( game.__next__() ) # 0
# or
print( next(game) ) # 5
print( next(game) ) # 10
print( next(game) ) # 15
print( next(game) ) # 20
print( next(game) ) # 25
game.close() # this will terminate our enless loop