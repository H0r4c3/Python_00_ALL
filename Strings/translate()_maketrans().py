'https://www.w3schools.com/python/ref_string_translate.asp'

'''
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.

If a character is not specified in the dictionary/table, the character will not be replaced.

If you use a dictionary, you must use ascii codes instead of characters.

string.translate(table)

Parameter:
table	Required. Either a dictionary, or a mapping table describing how to perform the replace
'''

# 1. Example = Use a mapping table to replace "S" with "P":

txt = "Hi, Sam!"
x = "mSa"
y = "eJo"
my_table = txt.maketrans(x, y)
print(txt.translate(my_table))


# 2. Example = The third parameter in the mapping table describes characters that you want to remove from the string:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
my_table = txt.maketrans(x, y, z)
print(txt.translate(my_table))


# 3. Example = The same example as above, but using a dictionary instead of a mapping table:

txt = "Good night Sam!"
my_dict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(my_dict))


# 4. Example = use a dictionary with ascii codes to replace 83 (S) with 80 (P):
my_dict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(my_dict))


# 5. Example
my_string = 'abcd efg'
translation_dict = {'a':'A', 'b':'H', 'e':'HH'}
my_table = my_string.maketrans(translation_dict)
my_string_changed = my_string.translate(my_table)
print(my_string_changed)


# 6. Example
# http://www.pythonchallenge.com/pc/def/map.html

old_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
x = 'yzabcdefghijklmnopqrstuvwx'
y = 'abcdefghijklmnopqrstuvwxyz'
my_table = old_string.maketrans(x, y)
new_string = old_string.translate(my_table)
print(new_string)

h = 'map'
t = h.maketrans(x, y)
print(h.translate(t))