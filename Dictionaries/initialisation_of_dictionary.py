'https://doughellmann.com/posts/the-performance-impact-of-using-dict-instead-of-in-cpython-2-7-2/'

import timeit

my_dict1 = {}

my_dict2 = dict()

time1 = timeit.timeit('{}')
print('Time for initialisation an empty dictionary using "{}" =', time1)

time2 = timeit.timeit('dict()')
print('Time for initialisation an empty dictionary using "dict()" =', time2)