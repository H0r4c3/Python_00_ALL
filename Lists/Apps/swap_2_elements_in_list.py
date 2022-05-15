'https://www.tutsmake.com/python-program-to-swap-two-elements-in-a-list/'


def swapPositions_1(list, pos1, pos2): 
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list)

new_list = swapPositions_1(my_list, 2, 3)
print(new_list)




def swapPositions_2(list, pos1, pos2):
    x = list.pop(pos1)
    y = list.pop(pos2-1)
    
    list.insert(pos1, y)
    list.insert(pos2, x)
    
    return list

my_list = ['a', 'b', 'c', 'd', 'e']
  
new_list_2 = swapPositions_2(my_list, 2, 3)
print(new_list_2)