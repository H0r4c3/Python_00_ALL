# complete the shorter strings with spaces to have a list with equal length strings

my_list = ['abc', 'defg', 'hijkl', 'mnopqr']

# the length of the longest string
max_len = len(max(my_list, key=len))
  
# the list of equal length strings  
equal_strings = [item + ' '*(max_len - len(item)) for item in my_list]

print(equal_strings)