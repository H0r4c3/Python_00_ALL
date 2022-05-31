'''
Having a list of lists, compare all item[0] and all item[1] and group items where for same item[0] the difference for item[1] = 1, and viceversa

Example:
my_list = [(0,1), (0,2), (1,2), (1,3), (1,5), (2,5)]

0 x x 0 0 0
0 0 x x 0 x
0 0 0 0 0 x

neighbours_set = [{(0,1), (0,2), (1,2), (1,3)}, {(1,5), (2,5)}]
'''

def neighbours(my_list):
    
    neighbours_list = [{my_list[0]}]
    
    def comparison(my_list, pos):
        ''' find the neighbours of the element from my_list in position pos'''
        neighbours_set = {my_list[pos]}
        for i in range(pos, len(my_list)):
            print(i, my_list[i])
            if (my_list[pos][0] == my_list[i][0] and abs(my_list[pos][1] - my_list[i][1]) == 1) or \
               (my_list[pos][1] == my_list[i][1] and abs(my_list[pos][0] - my_list[i][0]) == 1):
                neighbours_set.add(my_list[i])
    
        neighbours_list.append(neighbours_set)
            
        return neighbours_list
    
    
    for i in range(len(my_list)):
        neighbours_list = comparison(my_list, i)
        
    return neighbours_list


my_list = [(0,1), (0,2), (1,2), (1,3), (1,5), (2,5)]

neighbours_list = neighbours(my_list)
print(neighbours_list)

