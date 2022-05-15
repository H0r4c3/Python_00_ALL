'https://blog.finxter.com/the-sieve-of-eratosthenes-in-one-line-of-python/'


## Dependencies
from functools import reduce

def prime_numbers(n):
    primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2,n)))
    return primes

n = 100
primes = prime_numbers(n)
print(primes)