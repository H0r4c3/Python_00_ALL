'https://www.geeksforgeeks.org/gcd-in-python/'

'''
math.gcd(x, y)
Parameters : 
x :  Non-negative integer whose gcd has to be computed.
y : Non-negative integer whose gcd has to be computed.
Return Value : 
This method will return an absolute/positive integer value after 
calculating the GCD of given parameters x and y.
Exceptions : 
When Both x and y are 0, function returns 0, If any number is a character ,
Type error is raised.
'''

import math

# using math module
result = math.gcd(60, 48, 24)  
print(result)


# Using Euclidean Algorithm
def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
  
a = 60
b= 48
  
# prints 12
print ("The gcd of 60 and 48 is : ", end = "")
print (computeGCD(60, 48))