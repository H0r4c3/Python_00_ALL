'https://medium.com/@vanacorec/backtracking-and-crossword-puzzles-4abe195166f9'

'''
Factorial by Recursion
By definition, the factorial of n is equal to the product of n and all smaller positive integers. 
In order to use recursion to solve this, we need to break the problem down into “smaller problems of the same type.” 
We can do this by thinking of the factorial of n as n times the factorial of n-1. 
Then the factorial of n-1 is n-1 times the factorial of n-1-1… and so on until you hit the base case: factorial of 1 = 1.

5! = 5 * 4 * 3 * 2 * 1 = 120
5! = 5 * 4!
where 4! = 4 * 3!
where 3! = 3 * 2!
where 2! = 2 * 1!
where 1! = 1
Here is the python code for this:

def factorial(n):
    if n == 1:  #base case
        return 1
    else:   #recursive case
        return n * factorial(n-1)
    
factorial(5)
In this case, the base case is “if n == 1: return 1,” because we don’t need any more recursion to solve that problem. 
The function will continue to call itself until this base case is reached.
'''

def factorial(n):
    if n == 1:  #base case
        return 1
    else:   #recursive case
        return n * factorial(n-1)


result = factorial(5)
print(result)