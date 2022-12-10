

def replace_items_with_indices(my_list):
    my_list_indices = [idx for idx, item in enumerate(my_list)]
    
    return my_list_indices

my_list = [11, 11, 12, 13]
my_list_indices = replace_items_with_indices(my_list)
print(my_list_indices)