'''
Having a list of sets, reduce the list making unions betweens sets with common elements

Example:
neighbours_list = [{(0, 1)}, {(0, 1), (0, 2)}, {(0, 2), (1, 2)}, {(1, 2), (1, 3)}, {(1, 3)}, {(2, 5), (1, 5)}, {(2, 5)}]

Return:
union_list = [{(0, 1), (0, 2), (1, 2), (1, 3)}, {(1, 5), (2, 5)}]
'''

def together(neighbours_list):
    '''Having a list of sets, reduce the list making unions betweens sets with common elements'''
    
    union_list = [set(neighbours_list[0])]
    
    for item in neighbours_list[1:]:
        for new in union_list:
            if item.isdisjoint(union_list):
                union_list.append(item) #NOK!!!!!!!!!! - need to append only after parsing the entire union_list
        else:
            if item.isdisjoint(new):
                new = new.union(item)
                union_list.append(new)
        
    return union_list
        


neighbours_list = [{(0, 1)}, {(0, 1), (0, 2)}, {(0, 2), (1, 2)}, {(1, 2), (1, 3)}, {(1, 3)}, {(2, 5), (1, 5)}, {(2, 5)}]
#neighbours_list = [{(0, 1)}, {(0, 1), (0, 2)}, {(7,8)}, {(0, 1), (0, 3)}]

union_list = together(neighbours_list)
print(union_list)