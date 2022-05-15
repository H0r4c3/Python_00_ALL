'https://compucademy.net/recursion-in-python-programming/'

'''
Base case
A base case is essential with recursion. Without it there is no way for the algorithm to “know” when to stop. Not having one is like 
having a while True loop – i.e. you get an infinite loop, except with recursion, you will eventually hit your system’s maximum recursion limit. 
Here, the base case is when n <= 0.

Movement toward the base case
The algorithm must approach the base case on each successive call, otherwise it can not terminate. Again, comparing this to a while loop, 
not moving towards the base case is like not moving towards the condition for the while loop to exit. 
Each successive call here has n - 1 as its argument so we are approaching the base case.
'''

def factorial(n):
   if n == 1:
       return 1
   else:
       return n * factorial(n-1)

print(factorial(5))

'''
factorial(5) calls factorial(4) which calls factorial(3) etc, until the base case is reached (n == 1), then each of the function calls returns its value, 
in the reverse order to that in which they were called, until the value for the initial call factorial(5) is returned.

Here’s what happens before the final value of 120 is returned and printed:

|-- factorial(5)
|  |-- factorial(4)
|  |  |-- factorial(3)
|  |  |  |-- factorial(2)
|  |  |  |  |-- factorial(1)
|  |  |  |  |  |-- return 1
|  |  |  |  |-- return 2
|  |  |  |-- return 6
|  |  |-- return 24
|  |-- return 120
'''


# 1. without recursion
def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

print(fact(5))


# 2. without recursion
def fact(n):
    result = 1
    while n > 0:
        result = result * n
        n = n -1
    return result

print(fact(5))


# with recursion, but SHORTER:
def factorial(n):
    return n * factorial(n-1) if n else 1
    