'https://www.w3schools.com/python/ref_func_round.asp'

'''
The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

The default number of decimals is 0, meaning that the function will return the nearest integer.

round(number, digits)

number	Required. The number to be rounded
digits	Optional. The number of decimals to use when rounding the number. Default is 0.
'''
from math import e, pi
from decimal import Decimal, getcontext

x = round(5.76543, 2)
print(x)

x = round(5.76343, 2)
print(x)




print(f'e = {e}')
print(f'pi = {pi}')

# Set the precision of the decimal module
getcontext().prec = 100

# Define the values of e, pi, and the exponent
e = Decimal(e)
pi = Decimal(pi)

print(f'e = {e}')
print(f'pi = {pi}')

try:
    x = e**e**pi**pi
    print(f'e**e**pi**pi = {x}')
except:
    print('Exception')