'https://www.w3schools.com/python/ref_string_strip.asp'
'https://www.programiz.com/python-programming/methods/string/strip'


'''
The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

Syntax of String strip():

string.strip([chars])

strip() Parameters
chars (optional) - a string specifying the set of characters to be removed from the left and right part of the string.
The strip() method removes characters from both left and right based on the argument (a string specifying the set of characters to be removed).

Note: If the chars argument is not provided, all leading and trailing whitespaces are removed from the string.
'''

txt = "     banana     "
x = txt.strip()
print(x)

# Remove the leading and trailing characters
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

