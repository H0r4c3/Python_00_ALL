'https://www.delftstack.com/howto/python/python-lowercase-list/'

'''
Transform all chars in lowercase
'''

# 1. Solution:

def lower_lists_1(my_list):
    my_lower_list = list()

    for item in my_list:
        item2 = [x.lower() for x in item]
        my_lower_list.append(item2)
    
    return my_lower_list


my_list = [['A', 'B'], ['C', 'D']]

print(lower_lists_1(my_list))


# 2. Solution:

def lower_lists_2(my_list):
    my_lower_list = [list(map(lambda x: x.lower(), item)) for item in my_list]
    
    return my_lower_list
    
my_list = [['A', 'B'], ['C', 'D']]

print(lower_lists_2(my_list))
    

    