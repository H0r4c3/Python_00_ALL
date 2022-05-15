'https://www.kite.com/python/docs/re.escape'

'''
Return string with all non-alphanumerics backslashed; 
this is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it.
'''

import re
print(re.escape("Hello 123 .?!@ World"))
# OUTPUT:
# Hello\ 123\ \.\?\!\@\ World



# Remove punctuation from a string

import string

pattern = re.compile("[" + re.escape(string.punctuation) + "]")
print(pattern.sub("", "\"hello world!\", he's told me."))
# OUTPUT
# hello world hes told me