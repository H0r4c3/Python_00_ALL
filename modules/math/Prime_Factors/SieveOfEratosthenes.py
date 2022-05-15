'https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/'

# Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes

'''
Sieve of Eratosthenes:
The most efficient way to find all small primes was proposed by the Greek mathematician Eratosthenes. 
His idea was to make a list of positive integers not greater than n and sequentially strike out the 
multiples of primes less than or equal to the square root of n. After this procedure only primes are left in the list.
'''
 
def SieveOfEratosthenes(n):
    prime_numbers = list()
    
    # Create a boolean array "prime[0..n]" and initialize all entries it as true. 
    # A value in prime[i] will finally be false if i is Not a prime, else true.
    global prime
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Make a list with all prime numbers
    for p in range(n + 1):
        if prime[p]:
            prime_numbers.append(p)
            
    return prime_numbers


# https://blog.finxter.com/the-sieve-of-eratosthenes-in-one-line-of-python/
def SieveOfEratosthenes(n):
    
    # Initialize primary list:
    a = [True] * n    
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            # Mark non-prime
            for j in range(i*i, n, i):
                a[j] = False
                
 
# driver program
if __name__=='__main__':
    n = 30

    prime_numbers = SieveOfEratosthenes(n)
    print(f"Following are the prime numbers smaller than or equal to {n}: {prime_numbers}")
    