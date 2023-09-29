'''
re.sub(pattern, repl, string, count=0, flags=0)
Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. 
If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; if it is a string, any backslash escapes in it are processed. 
That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth.
'''

import re

my_string1 = 'Horacerac'

result1 = re.sub('rac', '', my_string1)           # Delete pattern rac (Replace pattern rac with '')
print(f'result1 = {result1}')

result2 = re.sub('rac', '123', my_string1)           # Replace pattern rac -> 123
print(result2)

my_string2 = 'H  o    r     a   c              e'
result22 = re.sub(r'\s+', ' ', my_string2)           # Eliminate duplicate whitespaces using wildcards
print(result22)

my_string3 = 'abcracdefghi'
result3 = re.sub('rac(def)ghi', r'\1', my_string3)    # Replace a string (racdefghi) with a part of itself = (def)
print(result3)

my_string4 = "The rain in Spain"
result44 = re.sub("\s", "9", my_string4, 2) # Replace space with '9', nr. of replacements = 2
print(result44)


my_string5 = 'MyFunctionName'
regex = '([a-z])([A-Z])'
result5 = re.sub(regex, r'\1_\2', my_string5)
print(f'my_string5 = {result5}') # Replace the upper letter with (lower letter + _)



def my_replace(i):
    if i==0:
        return 'Replacement000'
    return 'Replacement'

#result6 = re.sub('rac', my_replace(0), input)
#print(result6)



# Multiple replacements

my_string = 'adbcdefaabb'
my_replacements = [('a', '1'), ('b', '2')]

for old, new in my_replacements:
    my_string = re.sub(old, new, my_string)
    
print(my_string)


# Groups
# Replace the groups (lowercase) and (uppercase) with (lowercase + underscore(_)) and (uppercase + minus(-))
import re
old_string1 = 'ThisFunctionIsEmpty'
regex = '([a-z])([A-Z])' # one lowercase followed by an uppercase
new_string1 = re.sub(regex, r'\1_\2-', old_string1)
print(old_string1)
print(new_string1)
