'''
The unpacking operator (*) turns a list into positional arguments, print(*[1,2,3]) is the same as print(1,2,3)
This will print the items from the list separated by spaces.
'''

my_list = [1, 2, 3, 4, 5]
print(*my_list)


# Use unpacking for multiple assignment feature in Python
a, *b = [1, 2, 3, 4, 5]
print(a)
print(b)