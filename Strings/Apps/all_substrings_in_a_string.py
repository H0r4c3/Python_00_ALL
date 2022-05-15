# all substrings in a string

from itertools import combinations

def get_all_substrings(string):
    length = len(string) + 1
    
    return [string[x:y] for x, y in combinations(range(length), r=2)]

my_string = 'ABCDEFG'
print(get_all_substrings(my_string))