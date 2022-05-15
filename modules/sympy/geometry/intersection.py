'https://docs.sympy.org/latest/modules/geometry/utils.html'


'''
sympy.geometry.util.intersection(*entities, pairwise=False, **kwargs)[source]
The intersection of a collection of GeometryEntity instances.

Parameters
entities : sequence of GeometryEntity

pairwise (keyword argument) : Can be either True or False

Case 1: When the keyword argument ‘pairwise’ is False (default value): In this case, the function returns a list of intersections common to all entities.

Case 2: When the keyword argument ‘pairwise’ is True: In this case, the functions returns a list intersections that occur between any pair of entities.

Returns
intersection : list of GeometryEntity

Raises
NotImplementedError
When unable to calculate intersection.
'''

from sympy import Ray, Circle
from sympy.geometry.util import intersection

c = Circle((0, 1), 1)
print(intersection(c, c.center)) # -> []

right = Ray((0, 0), (1, 0))
up = Ray((0, 0), (0, 1))
print(intersection(c, right, up)) # -> [Point2D(0, 0)]
print(intersection(c, right, up, pairwise=True)) # -> [Point2D(0, 0), Point2D(0, 2)]

left = Ray((1, 0), (0, 0))
print(intersection(right, left)) # -> [Segment2D(Point2D(0, 0), Point2D(1, 0))]

