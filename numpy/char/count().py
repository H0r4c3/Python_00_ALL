'https://numpy.org/doc/stable/reference/generated/numpy.char.count.html'

'''
char.count(a, sub, start=0, end=None)[source]
Returns an array with the number of non-overlapping occurrences of substring sub in the range [start, end].

Calls str.count element-wise.

Parameters
a array_like of str or unicode
sub str or unicode
The substring to search for.

start, end int, optional
Optional arguments start and end are interpreted as slice notation to specify the range in which to count.

Returns
out ndarray
Output array of ints.
'''

import numpy as np

c = np.array(['aAaAaA', '  aA  ', 'abBABba'])

print(np.char.count(c, 'A'))

print(np.char.count(c, 'aA'))

print(np.char.count(c, 'A', start=1, end=4))

print(np.char.count(c, 'A', start=1, end=3))