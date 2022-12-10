'https://stackoverflow.com/questions/71475827/sort-a-list-according-to-the-sublists'


def sort_list_of_sublists(my_list):
    print(my_list)
    
    # Sort after first element in sublist
    my_list.sort()
    print(my_list)
    
    # Sort after second element in sublist
    my_list.sort(key=lambda sublist: sublist[1])
    print(my_list)
    
    return my_list
    

my_list = [[2, 2], [2, 1], [1, 2], [1, 1]]
result = sort_list_of_sublists(my_list)
print(result)