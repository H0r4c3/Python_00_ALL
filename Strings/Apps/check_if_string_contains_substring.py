'''
https://stackabuse.com/python-check-if-string-contains-substring/
https://itsmycode.com/how-to-check-if-string-contains-substring-in-python/
'''

fullstring = "StackAbusetackaaa"
substring = "tack"

# 1. The 'in' Operator

if substring in fullstring:
    print("Found!")
else:
    print("Not found!")

# 2. The String.index() Method
'This method is useful if you need to know the position of the substring'

position = fullstring.index(substring)
print(position)


# 3. The String.find() Method
'''
The String type has another method called find which is more convenient to use than index(), because we don't need to worry about handling any exceptions.
If find() doesn't find a match, it returns -1, otherwise it returns the left-most index of the substring in the larger string.
'''

position = fullstring.find(substring)
print(position)


# 4. Regular Expressions (RegEx)
'''
This method is best if you are needing a more complex matching function, like case insensitive matching. 
Otherwise, the complication and slower speed of regex should be avoided for simple substring matching use-cases.
'''

from re import search

if search(substring, fullstring):
    print("Found!")
else:
    print("Not found!")

    
# 5. String.count()
'The count() method checks for the occurrence of substring in a string. If the substring is not found in the string, it returns 0.'

print(fullstring.count(substring))


