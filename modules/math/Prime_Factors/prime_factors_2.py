'https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/'

# Python program to print prime factors
 
import math
 
# A function to print all prime factors of
# a given number n
def primeFactors(n):
    divisors = list()
    
    for i in range(2,n + 1):
        if n % i == 0:
            count = 1
            for j in range(2,(i//2 + 1)):
                if (i % j == 0):
                    count = 0
                    break
            if(count == 1):
                print(i)
                divisors.append(i)
                
    return divisors
         
# Driver Program to test above function
 
n = 315
n = 4
n1 = 2
n1 = 3
n = 6

divisors = primeFactors(n)
print(divisors)
print(len(divisors))