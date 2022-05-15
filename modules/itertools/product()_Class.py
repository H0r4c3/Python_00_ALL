'''
itertools.product() falls under the category called Combinatoric iterators of the Python itertools library.

itertools.product(*iterables, repeat=1):
It returns the cartesian product of the provided iterable with itself for the number of times specified by the optional keyword “repeat”. 
For example, product(arr, repeat=3) means the same as product(arr, arr, arr).
'''

from itertools import product
  
def cartesian_product(arr1, arr2):
    # return the list of all the computed tuple using the product() method
    return list(product(arr1, arr2)) 
    

if __name__ == "__main__": 
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
    
    # my function
    print(cartesian_product(arr1, arr2)) # -> [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
    
    # product Class
    print(list(product(arr1, arr2))) # -> [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
    
    print(list(product(arr1, repeat=2))) # -> [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

    print(list(product(range(0,9), repeat=2))) # product((0,1,2,3,4,5,6,7,8), (0,1,2,3,4,5,6,7,8)) = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), 
    # (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), 
    # (2, 8), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), 
    # (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 0), 
    # (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
