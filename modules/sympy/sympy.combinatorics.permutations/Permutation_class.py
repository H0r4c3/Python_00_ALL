'https://docs.sympy.org/latest/modules/combinatorics/permutations.html#sympy.combinatorics.permutations.Permutation.rank'

'''
The permutation of a given arrangement is given by indicating the positions of the elements after re-arrangement [R64]. 
For example, if one started with elements [x, y, a, b] (in that order) and they were reordered as [x, y, b, a] then the permutation would be [0, 1, 3, 2].
'''


# rank() method = Returns the lexicographic rank of the permutation.
from sympy.combinatorics.permutations import Permutation
p = Permutation([0, 1, 2, 3])
print(p)
print(p.rank())


p = Permutation([3, 2, 1, 0])
print(p)
print(p.rank())


# MORE METHODS to be ADDED!!!!!!!!!!!!!!!!