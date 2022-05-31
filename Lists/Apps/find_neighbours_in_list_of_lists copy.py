'''
Having a list of lists, compare all item[0] and all item[1] and group items where for same item[0] the difference for item[1] = 1, and viceversa

Example:
my_list = [(0,1), (0,2), (1,2), (1,3), (1,5), (2,5)]

0 x x 0 0 0
0 0 x x 0 x
0 0 0 0 0 x

neighbours_set = [{(0,1), (0,2), (1,2), (1,3)}, {(1,5), (2,5)}]
'''

my_list = [(0,1), (0,2), (1,2), (1,3), (1,5), (2,5)]

def neighbours(my_list):
    #neighbours_list = list()
    #neighbours_set = set()
    
    
    # def comparison(my_list, pos):
    #     neighbours_set = set()
    #     for i in range(pos, len(my_list)):
    #         neighbours_set.add(my_list[pos])
    #         print(i, my_list[i])
    #         if (my_list[pos][0] == my_list[i][0] and abs(my_list[pos][1] - my_list[i][1]) == 1) or \
    #            (my_list[pos][1] == my_list[i][1] and abs(my_list[pos][0] - my_list[i][0]) == 1):
    #             neighbours_set.add(my_list[i])
    #         print(neighbours_set)
    #     neighbours_list.append(neighbours_set)
    #     return neighbours_list
    
    neighbours_list = [{my_list[0]}]
    
    def comparison(my_list, pos):
        ''' find the neighbours of the element from my_list in position pos'''
        neighbours_set = set()
        for i in range(pos, len(my_list)):
            neighbours_set.add(my_list[pos])
            print(i, my_list[i])
            if (my_list[pos][0] == my_list[i][0] and abs(my_list[pos][1] - my_list[i][1]) == 1) or \
               (my_list[pos][1] == my_list[i][1] and abs(my_list[pos][0] - my_list[i][0]) == 1):
                neighbours_set.add(my_list[i])
            
        # for item in neighbours_list:
        #     print(f'intersection = {item.intersection(neighbours_set)}')
        #     if item.intersection(neighbours_set):
        #         item = item.union(neighbours_set)
        #     else:
        #         neighbours_list.append(neighbours_set)
        
        neighbours_list.append(neighbours_set)
        return neighbours_list
        
    neighbours_list = comparison(my_list, 0)
    neighbours_list = comparison(my_list, 1)
    neighbours_list = comparison(my_list, 2)
    neighbours_list = comparison(my_list, 3)
    neighbours_list = comparison(my_list, 4)
    neighbours_list = comparison(my_list, 5)
    
    # for i in range(1, len(my_list)):
    #     neighbours_set.add(my_list[0])
    #     print(i, my_list[i])
    #     if (my_list[0][0] == my_list[i][0] and abs(my_list[0][1] - my_list[i][1]) == 1) or (my_list[0][1] == my_list[i][1] and abs(my_list[0][0] - my_list[i][0]) == 1):
    #         neighbours_set.add(my_list[i])
    #     print(neighbours_set)
    # neighbours_list.append(neighbours_set)
    # print(neighbours_list)
    
    
    # for i in range(2, len(my_list)):
    #     neighbours_set.add(my_list[1])
    #     print(i, my_list[i])
    #     if (my_list[1][0] == my_list[i][0] and abs(my_list[1][1] - my_list[i][1]) == 1) or (my_list[1][1] == my_list[i][1] and abs(my_list[1][0] - my_list[i][0]) == 1):
    #         neighbours_set.add(my_list[i])
    #     print(neighbours_set)
    # neighbours_list.append(neighbours_set)
    # print(neighbours_list)
    
            
    return neighbours_list

neighbours_list = neighbours(my_list)
print(neighbours_list)

