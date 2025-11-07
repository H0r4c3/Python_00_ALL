def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
    for x in range(a, b):
        if isPrime(x):
            yield x

print(list(primeGenerator(2, 44)))