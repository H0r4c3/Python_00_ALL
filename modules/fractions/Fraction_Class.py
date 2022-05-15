'https://docs.python.org/3/library/fractions.html'

'''
The fractions module provides support for rational number arithmetic.

A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.

class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(float)
class fractions.Fraction(decimal)
class fractions.Fraction(string)
'''

from fractions import Fraction

print(Fraction(1.5))

print(Fraction(3, 5))

print(Fraction(5, 3))

print(Fraction(6, 12))

print(Fraction('3/7'))