'''
Split a list of lists into list of smaller lists over the first rows
For example:
[[0, 1, 2],
[3, 4, 5],
[6, 7, 8]]

splitted into:

[[0, 1],
[3, 4]]
and
[[1, 2],
[4, 5]]
'''

def split_list(my_list, new_length):
    list_of_lists = list()
    for i in range(len(my_list)-1):
        list_of_lists.append(my_list[i : i + new_length])
    
    return list_of_lists


def split_2D_list(my_list, rows, columns):
    list_of_lists = list()
    
    # row 0
    list0 = split_list(my_list[0], columns)
    print(list0)
    
    # row 1
    list1 = split_list(my_list[1], columns)
    print(list1)
    
    list_of_lists = zip(list0, list1)
    list_of_lists = list(map(list, list_of_lists))
    
    return list_of_lists



my_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(my_list)

list_of_lists = split_2D_list(my_list, 2, 2)
print(list_of_lists)