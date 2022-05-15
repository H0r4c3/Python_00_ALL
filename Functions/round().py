'https://www.w3schools.com/python/ref_func_round.asp'

'''
The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

The default number of decimals is 0, meaning that the function will return the nearest integer.

round(number, digits)

number	Required. The number to be rounded
digits	Optional. The number of decimals to use when rounding the number. Default is 0.
'''

x = round(5.76543, 2)
print(x)

x = round(5.76343, 2)
print(x)