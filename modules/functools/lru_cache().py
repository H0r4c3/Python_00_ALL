'https://www.geeksforgeeks.org/python-functools-lru_cache/'

'https://www.infoworld.com/article/3606188/speed-up-python-functions-with-memoization-and-lrucache.html'

'''
By default, lru_cache caches every call made to the function it wraps, so the cache can grow endlessly during a program’s runtime. 
If your function gets a restricted range of arguments (say, only the integers 1 through 100), you probably don’t have to worry about the cache growing too large. 
But in some cases you may want to restrict the cache to the top X number of possibilities to avoid exhausting the memory.
This is where the “lru” in lru_cache comes from. The “lru” stands for least recently used, and it describes how items in the cache are automatically cleared. 
Everything but the last X cached items is discarded.
To set the size of the cache for your function, just supply a number with the decorator, like so:

@lru_cache(360)
def sin_half(x):
    return sin(x)/2
This caches a maximum of 360 possible values for x, and their corresponding responses.

If you want to examine the statistics for a given function cache, use the .cache_info() method on the decorated function (e.g., sin_half.cache_info()). 
This reports the total number of cache hits and misses, the maximum cache size, and the current cache size, in that order.

You can also manually clear the cache on a decorated function with the .cache_clear() method.
'''


from functools import lru_cache
import time
import timeit
  
# Function that computes Fibonacci 
# numbers without lru_cache
def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n-1) + fib_without_cache(n-2)
      
# Execution start time
begin = time.time()
print(f'fib_without_cache(30) = {fib_without_cache(30)}')
  
# Execution end time
end = time.time()
  
print("Time taken to execute the function without lru_cache is", end-begin)

#my_time1 = timeit.timeit("fib_without_cache(30)", number = 5, globals = globals())
#print(f'my_time = {my_time1}')
  
# Function that computes Fibonacci
# numbers with lru_cache
@lru_cache(maxsize = 128)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)
      
begin = time.time()
print(f'fib_with_cache(300) = {fib_with_cache(300)}')
end = time.time()
  
print("Time taken to execute the function with lru_cache is", end-begin)

my_time2 = timeit.timeit("fib_with_cache(30)", number = 500_000, globals = globals())
print(f'my_time2 after 500_000 repetitions = {my_time2}')