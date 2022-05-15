my_list = [0, 1, 2, 3, 4, 5, 6]

# Reversing a list	
#Syntax: reversed_list = systems[start:stop:step] 
reversed_list = my_list[::-1]

# updated list
print('Reversed List: \n', reversed_list)

'''
a[start:stop]  # items start through (stop-1)
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
'''

print(my_list[1::-1])