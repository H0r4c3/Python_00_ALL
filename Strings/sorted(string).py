'''
Passing a string to sorted() returns a list containing the sorted characters as elements.
Use the join() method to concatenate a list of characters into a single string.
'''

org_str = 'cebad'

new_str_list = sorted(org_str)
print(org_str)
print(new_str_list)

new_str = ''.join(new_str_list)
print(new_str)
