'https://www.dataneb.com/post/what-is-the-most-efficient-way-to-find-prime-factors-of-a-number-python'

def is_prime(num):
    if num<2:
        return False
    else:
        return all(num % i for i in range(2, int(num ** 0.5) + 1))
    
    
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Another solution:

import numpy as np

def primes(n):
    x = np.ones((n+1,), dtype=np.bool_)
    x[0] = False
    x[1] = False
    for i in range(2, int(n**0.5)+1):
        if x[i]:
            x[2*i : : i] = False

    primes = np.where(x == True)[0]
    return primes


# n = int(input())

n = 1000

prime_list=[i for i in range(n) if is_prime(i)]
print(prime_list)

print(primes(n))