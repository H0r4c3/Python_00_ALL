
# Method 1

def group_consecutive(my_list):
    result = [(my_list[i], my_list[i+1]) for i in range(len(my_list)-1)]
    
    return result

my_list = [1, 2, 3, 4, 5, 6]
result = group_consecutive(my_list)
print(result)


# Method 2

from itertools import pairwise

my_list2 = [11, 12, 13, 14, 15, 16]
result2 = list(pairwise(my_list2))
print(result2)