'https://docs.sympy.org/latest/modules/geometry/ellipses.html#sympy.geometry.ellipse.Circle'

'https://www.geeksforgeeks.org/python-sympy-circle-method/'


'''
class sympy.geometry.ellipse.Circle(*args, **kwargs)[source]
A circle in space.

Constructed simply from a center and a radius, from three non-collinear points, or the equation of a circle.

Parameters
center : Point

radius : number or SymPy expression

points : sequence of three Points

equation : equation of a circle

Raises
GeometryError

When the given equation is not that of a circle. When trying to construct circle from incorrect parameters.
'''

#Example #1: Using center and radius

# import sympy and geometry module
from sympy.geometry import Point, Circle
  
# using Circle()
c1 = Circle(Point(0, 0), 5)
  
print(c1.hradius, c1.vradius, c1.radius) # -> (5, 5, 5)




# Example #2: using sequence of three points

# using Circle()
c2 = Circle(Point(0, 0), Point(1, 1), Point(1, 0))
  
print(c2.hradius, c2.vradius, c2.radius) # -> (sqrt(2)/2, sqrt(2)/2, sqrt(2)/2)



# Example #3: using equation of circle

from sympy import Eq

# using Circle()
c3 = Circle(x**2 + y**2 - 25, 0)
  
print(c3) # -> Circle(Point2D(0, 0), 5)