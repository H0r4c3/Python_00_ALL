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
# 1. Example

# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
  
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


# 2. Example

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)