'https://practice.geeksforgeeks.org/problems/number-of-subsets-with-product-less-than-k/1/'

from itertools import combinations
import numpy as np
from numpy.core.fromnumeric import prod

import bisect

class Solution:
    
    def numOfSubsets(self, arr, N, K):
        my_list = list(arr)
        arr = ' '.join(my_list)
        arr = np.fromstring(arr, dtype=int, sep=' ')
        counter = 0
        
        for i in range(1, N+1):
            for tup in combinations(arr, i):
                if prod(tup) <= K:
                    counter = counter + 1
                
        return counter
    
    def numOfSubsets2(self, arr, N, K):
        my_list = list(arr)
        arr = ' '.join(my_list)
        arr = np.fromstring(arr, dtype=int, sep=' ')
        counter = 0
        
        my_list_of_tuples = [tup for i in range(1, N+1) for tup in combinations(arr, i) if prod(tup) <= K]
                
        return len(my_list_of_tuples)
            
    
my_object = Solution()

N = 4
arr = '2453'
K = 12

print(my_object.numOfSubsets2(arr, N, K))


'''
from itertools import combinations

class Solution:
    
    
    def numOfSubsets(self, arr, N, K):
        print(arr)
        my_list = []
        for i in range(1, N+1):
            my_list = my_list + list(combinations(arr, i))
        print(combinations(arr, 2))

        
        print(my_list)
        counter = 0  
        for item in my_list:
            result = 1
            for x in item:
                result = result * x
            if result <= K:
                counter = counter + 1
                result = 1
            
        return(counter+N)
'''