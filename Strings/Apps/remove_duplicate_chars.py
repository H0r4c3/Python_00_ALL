'''
Example: String = 'ABCDEABBDDEEFFFFFAA'
Result = 'ABCDEF
'''

my_string = 'ABCDEABBDDEEFFFFFAA'

# fromkeys() method creates a dict having as keys each char from string and as value having None.
my_dict = dict.fromkeys(my_string)
print(my_dict)

my_string_without_duplicates = ''.join(my_dict)
print(my_string_without_duplicates)