'https://realpython.com/fibonacci-sequence-python/?__s=z6fw8dy8hh2ghqd22iv6'


'''
https://www.sanfoundry.com/python-program-print-nth-fibonacci-number-using-dynamic-programming-memoization/
Fibonacci numbers are defined by the sequence f(0) = 0, f(1) = 1 and f(n) = f(n – 1) + f(n – 2) for n >= 2. 
The program prompts the user to enter n and it prints the nth Fibonacci number.
'''

import timeit

# 1. Using recursion

def fibonacci_sequence(n):
    ''' Calculates the nth element from Fibonacci's Sequence'''
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

starttime = timeit.default_timer()
print("The start time is :", starttime)
print(f'Result = {fibonacci_sequence(30)}')
print("The end time is :", timeit.default_timer())
print("The time difference is :", timeit.default_timer() - starttime)

# time for 50_000 calculations
#my_time = timeit.timeit("fibonacci_sequence(10)", number = 50_000, globals = globals())
#print(my_time)


# 2. Without recursion 1

def fibo(n):
    fibo_list = [0, 1]
    if n==0:
        return [0]
    elif n==1:
        return [0, 1]
    else:
        for i in range(0, n-1):
            number = fibo_list[i] + fibo_list[i+1]
            fibo_list.append(number)
    
    print(fibo_list)        
    return fibo_list

print('Without recursion 1')
starttime = timeit.default_timer()
print("The start time is :", starttime)
print(f'Result = {fibo(30)[30]}')
print("The end time is :", timeit.default_timer())
print("The time difference is :", timeit.default_timer() - starttime)


# Without recursion 2

def fibo2(n):
    a = 0
    b = 1
    while (n-1):
        a, b = b, a+b
        print(a+b, end = " ")
        n = n - 1
    
    print()
    return a+b
        

print('Without recursion 2')
starttime = timeit.default_timer()
print("The start time is :", starttime)
print(f'Result = {fibo2(30)}')
print("The end time is :", timeit.default_timer())
print("The time difference is :", timeit.default_timer() - starttime)


# Using generator:
def fibo3(n):
    a = 0
    b = 1
    while a < n:
        yield a
        a, b = b, a+b
        
result = fibo3(10)
print(result.__next__)
        
