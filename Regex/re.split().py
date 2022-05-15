'https://betterprogramming.pub/split-vs-partition-in-python-strings-9505d070af55'

'https://docs.python.org/3.8/library/re.html#re.split'

'''
“Split string by the occurrences of pattern. 
If capturing parentheses are used in the pattern, then the text of all groups in the pattern are also returned as part of the resulting list. 
If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.”

re.split(pattern, string, maxsplit=0, flags=0)

Return type → List
'''

import re

print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)) # -> ['0', '3', '9']


s = "Hello Python"
print(re.split(" ", s)) # Output:['Hello', 'Python']


colors = "red-orange-yellow-purple"
print(re.split("-",colors)) #Output:['red', 'orange', 'yellow', 'purple']


# Spitting the string with multiple delimiters
print(re.split('[&$-]', colors))


# Splitting the string at the occurrences of any character other than alphanumerics (a-z, A-Z, 0–9) and underscore
print(re.split('\W', colors))


# Splitting the string at the occurrence of any character other than numbers
num="1,2%3&4!5@6"
print (re.split('\D',num)) #Output:['1', '2', '3', '4', '5', '6']


'''
str.split() → It’ll split the string by each occurrence of the delimiter (sep)
str.partition() → It’ll split the string on the first occurrences of the delimiter (sep)
str.rpartition() → It’ll split the string on the last occurrences of the delimiter (sep)
re.split() → It’ll split the string on the occurrences of the pattern. Multiple delimiters can be used to split the string.
'''