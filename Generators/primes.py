'https://github.com/ikokkari/PythonExamples/blob/master/generators.py'

# Prime numbers, remembering all the prime numbers generated so far. To
# test whether a number is prime, it is sufficient to test divisibility
# only by the smaller primes found so far.

def primes():
    _primes = [2, 3, 5, 7, 11, 13]
    # Handy syntactic sugar for yield inside for-loop
    yield from _primes
    curr = 17
    while True:
        for divisor in _primes:
            if curr % divisor == 0:
                break
            if divisor * divisor > curr:
                _primes.append(curr)
                yield curr
                break
        curr += 2
        
        
result = primes()

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))