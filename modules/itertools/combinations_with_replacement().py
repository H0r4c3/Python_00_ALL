'https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem'

'''
This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
'''

from itertools import combinations_with_replacement

my_list = [1, 2, 3, 4, 5]

print(list(combinations_with_replacement(my_list, 3)))

my_string = 'ABCDEFG'
print(list(combinations_with_replacement(my_string, 2)))