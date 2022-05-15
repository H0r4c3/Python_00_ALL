'https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods'

'''
Python’s built-in function chr() is used for converting an Integer to a Character, 
while the function ord() is used to do the reverse, i.e, convert a Character to an Integer.
c = chr(i)
The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in Hexadecimal). ValueError will be raised if the integer i is outside that range.
'''
y = chr(65)
print(y)


start = 0
end = 1114111
 
try:
    for i in range(start, end+2):
        a = chr(i)
except ValueError:
    print("ValueError for i =", i)


'''
The ord() function takes a string argument of a single Unicode character and returns its integer Unicode code point value. It does the reverse of chr().
i = ord(c)
This raises a TypeError if the length of the input string is not equal to one.
'''

y = ord('A')
print(y)


alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
# Print 65-90
for i in alphabet_list:
    print(ord(i), end = " , ")