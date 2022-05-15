'https://www.geeksforgeeks.org/filter-in-python/'

'''
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax:
filter(function, sequence)

Parameters:
function: function that tests if each element of a sequence true or not.
sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.

Returns:
returns an iterator that is already filtered.
'''

input_list = '!abcd?efg!h'
filt = filter(lambda ch: ch not in " ?.!/;:", input_list)

my_list = list(filt)
my_string = ''.join(my_list)
print(my_string)