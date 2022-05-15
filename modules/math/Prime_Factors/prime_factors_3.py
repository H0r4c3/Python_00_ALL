'https://paulrohan.medium.com/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f'

import math

def get_prime_factors(number):
    # create an empty list and later I will
    # run a for loop with range() function using the append() method to add elements to the list.
    prime_factors = []

    # First get the number of two's that divide number
    # i.e the number of 2's that are in the factors
    
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    # After the above while loop, when number has been
    # divided by all the 2's - so the number must be odd at this point
    # Otherwise it would be perfectly divisible by 2 another time
    # so now that its odd I can skip 2 ( i = i + 2) for each increment
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i


    # Here is the crucial part.
    # First quick refreshment on the two key mathematical conjectures of Prime factorization of any non-Prime number
    # Which is - 1. If n is not a prime number AT-LEAST one Prime factor would be less than sqrt(n)
    # And - 2. If n is not a prime number - There can be AT-MOST 1 prime factor of n greater than sqrt(n).
    # Like 7 is a prime-factor for 14 which is greater than sqrt(14)
    # But if the above loop DOES NOT go beyond square root of the initial n.
    # Then how does that greater than sqrt(n) prime-factor
    # will be captured in my prime factorization function.
    # ANS to that is - in my first for-loop I am dividing n with the prime number if that prime is a factor of n.
    # Meaning, after this first for-loop gets executed completely, the adjusted initial n should become
    # either 1 or greater than 1
    # And if n has NOT become 1 after the previous for-loop, that means that
    # The remaining n is that prime factor which is greater that the square root of initial n.
    # And that's why in the next part of my algorithm, I need to check whether n becomes 1 or not,
    
    if number > 2:
        prime_factors.append(int(number))

    return prime_factors

print(get_prime_factors(4))


'''
The Algorithm / Steps
1> I start the divisor to be the smallest prime number, which is 2. Divide by 2 as many times as I can, until I can no longer divide by 2. (And during this process, record the number of times I can successfully divide.)
Further on shy I am dividing or adjusting the initial number in the above
number /= prime_num
Say, if I do not divide — prime factors with greater than 1 multiplicity will result in the larger factor being non-prime. I dont want to consider about 2*n or 3*n because I have already checked and captured in my prime_factor list for 2 and 3
So, to solve the above problem, I keep dividing the larger factor of a pair by the smaller one until it no longer divides.
2> So with each successive while loop I am dividing the number by successively larger primes until I find one that is a factor of the number.
That is after the first division by 2 (assuming I found 2 to be a factor of the initial number), take the result from (1) i.e. the adjusted number after dividion by 2, and divide by 3 as many times as I can.
Then go to the next prime number, 5. Take the result from (2), and divide by 5 as many times as I can.
And during this successive divisions, as soon as I have found a factor or divisor, p , I can replace n with m=n/p and continue the process of trial division with primes greater than or equal to p up to (n/p)¹/2
Repeat the process, until final result is 1.
Now the most important part for improving time-complexity of the algorithm — which follows from the principle that -
In prime factorization of n the loop goes upto square root of n and not till n.
3> However, we don’t need to go out that far i.e. upto the number itself. If we’ve tested all the primes up to the square root of our target number without finding a divisor, we don’t need to go any further because we know that our target number is prime after all.
This is because — If a number N has a prime factor larger than √n , then it surely has a prime factor smaller than √n
So, it’s sufficient to search for prime factors in the range [1, sqrt(n)], and then use them in order to compute the prime factors in the range [sqrt(n), n].
The way we implement the above is as follows -
A. We know that prime factors with >1 multiplicity will result in the larger factor being non-prime. To solve this, keep dividing the larger factor of a pair by the smaller one until it no longer divides.
B. As an example: For 28, factors are 2,2,7, here 7 is larger than sqroot(28), but there is no single prime number that can combine to form 28 (i.e. x*7=28, where x is prime, this does not exist, since x is 4 which is not prime), so dividing the primes from beginning with 2 multiple time will help, 28/2= 14, 14/2 = 7, then we know the 2 & 2 are prime factors, also take the remaining one 7 is also another prime number completing the prime factor list.
If no prime factors exist in the range [1, sqrt(n)], then “n” itself is prime and there is no need to continue searching beyond that range.
To explain a little more on this — If you do not find a factor less than sqrt(n), then the number “n” itself is a prime number. Because, consider the opposite, you find two factors larger than sqrt(n), say “a” and “b”. But then a * b > sqrt(n) * sqrt(n) making their product larger than the number itself which is impossible.
Therefore, if there is a factor larger than sqrt(n), there must also exist a factor smaller than sqrt(n), otherwise their product would exceed the value of “n”.
But in this case it will make the variable ‘prime_num’ NON-PRIME — Because now itcan be expressed it as ( a * b ) which is only possible for NON-Prime number, as a Prime number can only be expressed as 1 * itself.
But here we are ONLY interested in finding Prime factors, and so will ignore all NON-PRIME FACTORS.
Hence in the above Algorithm, checking all the possible prime-number upto the math.sqrt(number) is sufficient
'''