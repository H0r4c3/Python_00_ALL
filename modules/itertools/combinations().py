'''
itertools.combinations(iterable, r)

This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
'''

from itertools import combinations

my_list = [1, 2, 3, 4, 5]

print(list(combinations(my_list, 2)))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

print(list(combinations(my_list, 3)))
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]


my_string = 'ABCDEFG'
print(list(combinations(my_string, 4)))


# all combinations in reversed order (from biggest, to smallest)
my_string = 'ABCDEFG'
all_comb = [''.join(item) for i in range(len(my_string), 0, -1) for item in combinations(my_string, i)]
print(all_comb)


# all substrings in a string

def get_all_substrings(string):
    length = len(string) + 1
    print(list(combinations(range(length), r=2)))
    
    return [string[x:y] for x, y in combinations(range(length), r=2)]

my_string = 'ABCDEFG'
print(get_all_substrings(my_string))