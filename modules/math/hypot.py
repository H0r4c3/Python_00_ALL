'https://docs.python.org/3/library/math.html'
'https://www.geeksforgeeks.org/python-math-function-hypot/'

'''
math.hypot(*coordinates)
Return the Euclidean norm, sqrt(sum(x**2 for x in coordinates)). This is the length of the vector from the origin to the point given by the coordinates.

For a two dimensional point (x, y), this is equivalent to computing the hypotenuse of a right triangle using the Pythagorean theorem, sqrt(x*x + y*y).

Changed in version 3.8: Added support for n-dimensional points. Formerly, only the two dimensional case was supported.

Changed in version 3.10: Improved the algorithm’s accuracy so that the maximum error is under 1 ulp (unit in the last place). 
More typically, the result is almost always correctly rounded to within 1/2 ulp.
'''

# Import the math module
import math
  
# Use of hypot function
print("hypot(3, 4) : ", math.hypot(3, 4))
  
# Neglects the negative sign
print("hypot(-3, 4) : ", math.hypot(-3, 4))
  
print("hypot(6, 6) : ", math.hypot(6, 6))