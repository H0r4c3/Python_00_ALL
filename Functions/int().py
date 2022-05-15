'https://www.tutorialsteacher.com/python/python-int'

'''
The int() function returns integer object from a float or a string containing digits.
int() Parameters
int() method takes two arguments:

x - Number or string to be converted to integer object.
The default argument is zero.
base - Base of the number in x.
Can be 0 (code literal) or 2-36.

Return value from int()
int() method returns:

an integer object from the given number or string treats default base as 10
(No parameters) returns 0
(If base given) treats the string in the given base (0, 2, 8, 10, 16)
'''

# binary 0b or 0B
print("For 1010, int is:", int('1010', 2))
print("For 0b1010, int is:", int('0b1010', 2))

# octal 0o or 0O
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))

# hexadecimal
print("For A, int is:", int('A', 14))
print("For 0xA, int is:", int('0xA', 16))