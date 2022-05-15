'https://docs.python.org/3/library/math.html'

'''
math.ceil(x)
Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x.__ceil__(), which should return an Integral value.

math.floor(x)
Return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__(), which should return an Integral value.

math.trunc(x)
Return the Real value x truncated to an Integral (usually an integer). Delegates to x.__trunc__().
'''

import math

# rounding

# rounds up
print(math.ceil(5.43))

# rounds down
print(math.floor(5.43))

# truncate
print(math.trunc(5.43))

# negative number
print(math.ceil(-5.43))