'https://www.geeksforgeeks.org/python-ways-to-determine-common-prefix-in-set-of-strings/'
'https://stackoverflow.com/questions/6718196/determine-prefix-from-a-set-of-similar-strings'

# 1. Method: Using Naive Approach

my_string = ['akshat', 'akash', 'akshay', 'akshita']
 
res = ''
prefix = my_string[0]
 
for string in my_string[1:]:
    while string[:len(prefix)] != prefix and prefix:
        prefix = prefix[:len(prefix)-1]
    if not prefix:
        break
    
common_prefix = prefix
print(f'The common prefix is: {common_prefix}')



# 2. Method: Using itertools.takewhile and zip 

from itertools import takewhile
 
my_string2 = ['my_prefix_what_ever', 'my_prefix_what_so_ever', 'my_prefix_doesnt_matter']

char_tuples = zip(*my_string2)
#print(list(char_tuples))

prefix_tuples = takewhile(lambda x : all(x[0] == y for y in x), char_tuples)

common_prefix = ''.join(c[0] for c in prefix_tuples)
print(f'The common prefix is: {common_prefix}')


# 3. Method: using os.path

from os import path

my_string = ['akshat', 'akash', 'akshay', 'akshita']

common_prefix = path.commonprefix(my_string)
print(f'The common prefix is: {common_prefix}')