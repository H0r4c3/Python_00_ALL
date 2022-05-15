'''
Create a list of all rotated lists
'''

def rotate_list(my_list):
    list_of_lists = list()
    for _ in range(len(my_list)):
        my_list = my_list[1:] + my_list[:1]
        list_of_lists.append(my_list)
    
    return list_of_lists


my_list = [0, 1, 2, 3, 4]
list_of_lists = rotate_list(my_list)
print(list_of_lists)
