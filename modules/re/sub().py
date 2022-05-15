'''
re.sub(pattern, repl, string, count=0, flags=0)
Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. 
If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; if it is a string, any backslash escapes in it are processed. 
That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth.
'''

import re

input1 = 'Horace'

result1 = re.sub('rac', '', input1)           # Delete pattern rac
print(result1)

result2 = re.sub('rac', '123', input1)           # Replace pattern rac -> 123
print(result2)

input2 = 'H  o    r     a   c              e'
result22 = re.sub(r'\s+', ' ', input2)           # Eliminate duplicate whitespaces using wildcards
print(result22)

input3 = 'abcracdefghi'
result3 = re.sub('rac(def)ghi', r'\1', input3)    # Replace a string with a part of itself
print(result3)

input4 = "The rain in Spain"
result44 = re.sub("\s", "9", input4, 2) # Replace space with '9', nr. of replacements = 2
print(result44)



def my_replace(i):
    if i==0:
        return 'Replacement000'
    return 'Replacement'

result5 = re.sub('rac', my_replace(0), input)
print(result5)
