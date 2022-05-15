'https://docs.python.org/3/library/itertools.html#itertools.pairwise'

'''
Return successive overlapping pairs taken from the input iterable.

The number of 2-tuples in the output iterator will be one fewer than the number of inputs. It will be empty if the input iterable has fewer than two values.

Roughly equivalent to:

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
'''



# Split a number into equal parts given the number of parts
import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b, c, d = itertools.tee(iterable, 4)
    next(a, b)
    next(b, c)
    next(c, d)
    return zip(a, b, c, d)

my_list = [1, 10000]
print(list(pairwise(my_list)))


# Example:
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = itertools.pairwise(my_list)
print(list(result)) # -> [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]