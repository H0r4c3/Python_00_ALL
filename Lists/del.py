'''
del my_list[index]
del my_list[a : b] - This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.

'''

my_list = ['cat', 'dog', 'rabbit', 'guinea pig']

# delete the item with index 2
del my_list[2]
print(my_list)



my_list = ['cat', 'dog', 'rabbit', 'guinea pig']

del my_list[2:4]
print(my_list)