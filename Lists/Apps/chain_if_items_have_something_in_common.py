'''
Compare each set in a list with the rest of sets, and, if they have something in common, unite them
    
For example:
my_list = [{1}, {2, 3}, {3, 4}, {2, 3, 4}, {5, 6}, {6, 7}]
result = [{1}, {2, 3, 4}, {5, 6, 7}]
'''



def chain_common_elements(my_list):
    '''
    Compare each set in a list with the rest of sets, and, if they have something in common, unite them
    '''
    
    for i in range(len(my_list)-1):
        groups = list()
        print(f'i_my_list[i] = {my_list[i]}')
        for j in range(i+1, len(my_list)):
            print(f'my_list[j] = {my_list[j]}')
            if not my_list[i].isdisjoint(my_list[j]):
                print('Chain')
                my_list[i] = my_list[i].union(my_list[j])
                my_list[j] = my_list[i]
                
    my_list = list(map(tuple, my_list))
    groups = list(dict.fromkeys(my_list))
    return groups
    
my_list = [{1}, {2, 3}, {3, 4}, {2, 3, 4}, {5, 6}, {6, 7}]
groups = chain_common_elements(my_list)
groups = list(map(sorted, groups))
print(groups)
    
    