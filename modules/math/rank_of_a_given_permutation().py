'https://johnlekberg.com/blog/2020-03-04-permutation-rank.html'

import math

def permutation_position_quick(word):
    '''
    Returns the rank of the permutation:
    For example: 012 is the first permutation, 021 is the second permutation
    Input: the permutation
    Output: the rank of that permutation 
    '''
    N = len(word)
    
    first = sorted(word)
    
    chars_before = {
        first[i]: first[:i]
        for i in range(N)
    }
    
    count = 0
    for i in range(N):
        possible_chars = set(chars_before[word[i]])
        possible_chars.difference_update(word[:i])
        n_wildcards = N - (i + 1)
           
        count += (
          len(possible_chars) * math.factorial(n_wildcards)
        )
    
    return 1 + count

print(permutation_position_quick('021'))