
from itertools import groupby

def check_consecutives(my_list, repetitions):
    #result = any(sum(1 for _ in g) > 1 for _, g in groupby(my_list))
    result = any(sum(1 for item in rep) >= repetitions for item, rep in groupby(my_list))
    
    g = groupby(my_list)
    for _, rep in g:
        print(list(rep))
    
    return result

my_list = [1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6]
result = check_consecutives(my_list, 4)
print(result)