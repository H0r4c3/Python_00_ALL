'https://docs.python.org/2/library/difflib.html#difflib.ndiff'

'''
difflib.ndiff(a, b[, linejunk][, charjunk])

Compare a and b (lists of strings); return a Differ-style delta (a generator generating the delta lines).

Optional keyword parameters linejunk and charjunk are for filter functions (or None):

linejunk: A function that accepts a single string argument, and returns true if the string is junk, or false if not. The default is (None), starting with Python 2.3. 
Before then, the default was the module-level function IS_LINE_JUNK(), which filters out lines without visible characters, except for at most one pound character ('#'). 
As of Python 2.3, the underlying SequenceMatcher class does a dynamic analysis of which lines are so frequent as to constitute noise, and 
this usually works better than the pre-2.3 default.

charjunk: A function that accepts a character (a string of length 1), and returns if the character is junk, or false if not. 
The default is module-level function IS_CHARACTER_JUNK(), which filters out whitespace characters (a blank or tab; note: bad idea to include newline in this!).

'''
from difflib import ndiff

a = 'abcdefg'
b = 'aacddfg'

dif = ndiff(a, b)
print(list(dif))