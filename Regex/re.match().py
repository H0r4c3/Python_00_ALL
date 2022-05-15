'https://www.guru99.com/python-regular-expressions-complete-tutorial.html'

'''
re.match() function of re in Python will search the regular expression pattern at the BEGINNING of the string and return the first occurrence. 
The Python RegEx Match method checks for a match only at the beginning of the string. 
So, if a match is found in the first line, it returns the match object. 
But if a match is found in some other line, the Python RegEx Match function returns null.

For example, consider the following code of Python re.match() function. 
The expression “w+” and “\W” will match the words starting with letter ‘g’ and thereafter, anything which is not started with ‘g’ is not identified. 
To check match for each element in the list or string, we run the for loop in this Python re.match() Example.
'''

import re

my_list = ['guru99 get', 'guru99 give', 'guru Selenium']

for item in my_list:
    z = re.match('(g\w+)\W(g\w+)', item)
    
    if z:
        print(z.groups())