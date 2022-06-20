'''
This method creates a dictionary having key = item in list, value = neighbors of item
'''

def find_neighbors(my_list):
    neighbors = dict()
    if len(my_list) == 1:
        return {my_list[0] : my_list[0]}
    for item in my_list:
        pos = my_list.index(item)
        if pos == 0:
            neighbors[item] = [my_list[pos+1]]
        elif pos == len(my_list) - 1:
            neighbors[item] = [my_list[pos-1]]
        else:
            neighbors[item] = [my_list[pos-1], my_list[pos+1]]        
    
    print(neighbors)
    return neighbors

my_list = [1, 2, 3, 4, 5, 6]
#my_list = [1]
neighbors = find_neighbors(my_list)
print(neighbors)