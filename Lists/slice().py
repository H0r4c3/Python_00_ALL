'''
A negative number used for the start of the slice will return a list which contains the number of items starting from the end of the list. 
A negative number used for the end returns a list which contains items excluding the number of items at the end of the list.
'''

# Examples:

colors = ['red', 'green', 'blue', 'yellow', 'orange']

print(colors[:4])
print(colors[1:4:2])

# List containing only last 2 = ['yellow', 'orange']
print(colors[-2:])

# List excluding last 2 = ['red', 'green', 'blue']
print(colors[:-2])


# Example (reversing a list):

colors = ['red', 'green', 'blue', 'yellow', 'orange']
colors_reversed = colors[::-1]
print(colors_reversed)


# Modifying a list using slice
# Initialize list
List = [0, 1, 2, 3, 4]
List[1:4] = ['one', 'two', 'three']
print(List)


# print the list, alternatively, normal and backwards
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
for i in range(6):
    my_list_new = my_list[::(-1)**i]
    print(my_list_new)
