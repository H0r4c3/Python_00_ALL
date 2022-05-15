'https://medium.com/dev-today/the-single-most-useful-python-decorator-cache-88086c07417e'
'https://docs.python.org/3/library/functools.html'

'''
@functools.cache(user_function)

Simple lightweight unbounded function cache. Sometimes called “memoize”.

Returns the same as lru_cache(maxsize=None), creating a thin wrapper around a dictionary lookup for the function arguments. 
Because it never needs to evict old values, this is smaller and faster than lru_cache() with a size limit.

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

>>> factorial(10)      # no previously cached result, makes 11 recursive calls
3628800
>>> factorial(5)       # just looks up cached value result
120
>>> factorial(12)      # makes two new recursive calls, the other 10 are cached
479001600
'''

def factorial(n):
    return n * factorial(n-1) if n else 1


# Now, we need to measure the how long it will take:
import timeit
#import sys
#sys.setrecursionlimit(5000)
def factorial(n):
    return n * factorial(n-1) if n else 1

my_time = timeit.timeit("factorial(6)", number = 500_000, globals = globals())
print(f'factorial(6) repeated 500_000 times = {my_time} seconds')
    
    
# Now, let’s just add the decorator @cache to our method, and see again how it behave:
import timeit
from functools import cache
#import sys
#sys.setrecursionlimit(5000)

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

my_time = timeit.timeit("factorial(6)", number = 500_000, globals = globals())
print(f'factorial(6) repeated 500_000 times using @cache = {my_time} seconds')

