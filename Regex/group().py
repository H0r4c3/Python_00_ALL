'https://www.geeksforgeeks.org/re-matchobject-group-function-in-python-regex/'

'''
re.MatchObject.group() method returns the complete matched subgroup by default or a tuple of matched subgroups depending on the number of arguments
'''

import re
 
"""We create a re.MatchObject and store it in match_object variable
   the '()' parenthesis are used to define a specific group"""
 
match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')
 
""" w in above pattern stands for alphabetical character
    + is used to match a consecutive set of characters satisfying a given condition
    so w+ will match a consecutive set of alphabetical characters"""
 
# for entire match
print(match_object.group())
# also print(match_object.group(0)) can be used
 
# for the first parenthesized subgroup
print(match_object.group(1))
 
# for the second parenthesized subgroup
print(match_object.group(2))
 
# for the third parenthesized subgroup
print(match_object.group(3))
 
# for a tuple of all matched subgroups
print(match_object.group(1, 2, 3))





# My Example
# Matches every word after a 'keyword=' -> 'light' (the keyword is 'theme')
my_string = 'theme=light; sessionToken=abc123'
keyword = 'theme'
#pattern = re.compile(keyword + '=([\w]+)')
pattern = re.compile('theme=([\w]+)')
result = pattern.search(my_string).group(1)
print(result)