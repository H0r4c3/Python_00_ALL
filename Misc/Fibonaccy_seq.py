'https://realpython.com/fibonacci-sequence-python/?__s=z6fw8dy8hh2ghqd22iv6'


'''
https://www.sanfoundry.com/python-program-print-nth-fibonacci-number-using-dynamic-programming-memoization/
Fibonacci numbers are defined by the sequence f(0) = 0, f(1) = 1 and f(n) = f(n – 1) + f(n – 2) for n >= 2. 
The program prompts the user to enter n and it prints the nth Fibonacci number.
'''


from functools import lru_cache

@lru_cache(maxsize = 128)
def calc_fibo(n):
    fibo = list()
    if n < 2:
        return n
    
    elem = calc_fibo(n-1) + calc_fibo(n-2)
    
    fibo.append(elem)
    return elem

n = 5
fibo = list()
for item in range(n+1):
    fibo.append(calc_fibo(item))
elem = calc_fibo(n)
print(elem)
print(fibo)