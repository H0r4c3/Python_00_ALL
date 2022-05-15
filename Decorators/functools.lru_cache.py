'https://python.plainenglish.io/pythons-amazing-functools-module-3c4602f09b15'


from functools import lru_cache
from time import time

@lru_cache(maxsize=128)
def fibo_lru(n):
   if n <= 1:
       return n
   else:
       return(fibo_lru(n-1) + fibo_lru(n-2))
   
   
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
   
   
def sum_of_fibo(nterms,fun):
    start = time()
    result = 0
    for i in range(nterms):
        result += fun(i)
    print(f'Total Sum {result} , Total time taken {time() - start} sec')
    

'''
“lru_cache” decorator can save us a lot of time when we need to perform computationally expensive or I/O bound operations through a function.
LRU stands for Least Recently Used, it saves the result of last executed function in memory and when it have to again execute the function, 
first it will check in cache, if found it will return the result otherwise it will go on to execute the function.
Just applying the “lru_cache” decorator over a function will make the above algorithm execute crazy fast.
'''