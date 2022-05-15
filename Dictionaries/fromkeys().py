'Create a dictionary, using the List items as keys.'
'Create a dictionary, using the String items as keys.'

''' 
fromkeys() method creates a dict having as keys each char from string and as value having None or the value specified.
'''

my_list = ["a", "b", "a", "c", "c"]
my_dict = dict.fromkeys(my_list, 'value')
print(my_dict)


my_string = 'ABCDEABBDDEEFFFFFAA'
# fromkeys() method creates a dict having as keys each char from string and as value having None.
my_dict = dict.fromkeys(my_string)
print(my_dict)

my_list = [1, 2, 3, 4, 5, 6]
def value_func(x):
    return x*2
value = value_func(1)
my_dict = dict.fromkeys(my_list, value)
print(my_dict)