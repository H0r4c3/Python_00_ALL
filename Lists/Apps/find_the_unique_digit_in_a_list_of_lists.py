'''
Find the unique elements in a list of lists. Must be in a list, not alone in that list.
'''

def find_unique_digit(my_list):
    
    # eliminate the digit not in a list and the list with len = 1
    new_list = [item for item in my_list if type(item) == list and len(item) > 1]
    print(new_list)

    # flatten the list
    my_list_flat = [item for sublist in new_list for item in sublist]
    print(my_list_flat)

    # find the unique digit
    unique_digit = [item for item in my_list_flat if my_list_flat.count(item) == 1]
    print(unique_digit)

    # find the index of the unique digit
    for item in my_list:
        if type(item) == list and len(item) > 1:
            if unique_digit[0] in item:
                idx = my_list.index(item)
    
    return unique_digit[0], idx

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2], [5, 6], [7, 9], 3, [3]]

unique_digit, idx = find_unique_digit(my_list)
print(unique_digit)
print(idx)

