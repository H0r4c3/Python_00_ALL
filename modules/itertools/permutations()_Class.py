'''
itertools.permutations(iterable[, r])

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
'''

from itertools import permutations

print(list(permutations(['1','2','3']))) # -> [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]

print(list(permutations(['1','2','3'], 2))) # -> [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

print(list(permutations(range(0,3), 2))) # -> [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

