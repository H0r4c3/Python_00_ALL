'https://docs.python.org/3/library/functions.html#int'

'''
class int(x, base=10)

If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in radix base.
'''

my_string = '1111'

new_string = int(my_string, 2)
print(new_string)