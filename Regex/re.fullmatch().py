'https://www.geeksforgeeks.org/re-fullmatch-function-in-python/'

'''
re.fullmatch() returns a match object if and only if the entire string matches the pattern. Otherwise, it will return None. 
The flag at the end is optional and can be used to ignore cases etc. 

Syntax: re.fullmatch(pattern, string, flags=0)

Parameters:
pattern: the regular expression pattern that you want to match.
string: the string which you want to search for the pattern.
flags (optional argument): a more advanced modifier that allows you to customize the behavior of the function. 
'''

import re
  
  
string = 'geeks'
pattern = 'g...s'
  
print(re.fullmatch(pattern, string))


'''
Difference Between re.match() and re.fullmatch()
re.fullmatch() and re.match() both are functions of re module in python. These functions are very efficient and fast for searching in strings. 
Both functions attempt to match at the beginning of the string.  
But the difference between re.match() and re.fullmatch() is that re.match() matches only at the beginning but re.fullmatch() tries to match at the end as well.
'''

import re
  
  
string = "Geeks for geeks"
pattern = "Geeks"
  
print(re.match(pattern, string))
print(re.fullmatch(pattern, string))
print(re.findall(pattern, string))
