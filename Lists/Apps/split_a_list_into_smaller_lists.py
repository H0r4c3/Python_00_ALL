import numpy as np
def split_list(my_list, new_length):
    new_lists = list()
    for i in range(len(my_list)):
        new_lists.append(my_list[i : i + new_length])
    
    return new_lists

my_list = [0, 1, 2, 3, 4, 5, 6]
my_list = np.array(my_list)
new_lists = split_list(my_list, 2)

print(my_list)
print(new_lists)