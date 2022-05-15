'https://stackoverflow.com/questions/15347174/python-finding-prime-factors'


# 1. Method
def prime_factors(n):
    prime_fac = list()
    
    for i in range(2, n + 1):
        if n % i == 0:
            count = 1
            for j in range(2, (i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                print(i)
                prime_fac.append(i)
    return prime_fac

# 2. Method
from sympy.ntheory import factorint

def prime_factors_2(n):
    prime_fac = factorint(n, multiple=True)
    return prime_fac


         
n = 6              
prime_fac1 = prime_factors(n)
print(prime_fac1)

prime_fac2 = prime_factors_2(n)
print(prime_fac2)
