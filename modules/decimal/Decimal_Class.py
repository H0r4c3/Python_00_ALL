'https://docs.python.org/3/library/decimal.html?highlight=decimal%20class#decimal.Decimal'

'''
class decimal.Decimal(value='0', context=None)

Construct a new Decimal object based from value.

value can be an integer, string, tuple, float, or another Decimal object. If no value is given, returns Decimal('0'). 
If value is a string, it should conform to the decimal numeric string syntax after leading and trailing whitespace characters, as well as underscores throughout, 
are removed:

sign           ::=  '+' | '-'
digit          ::=  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
indicator      ::=  'e' | 'E'
digits         ::=  digit [digit]...
decimal-part   ::=  digits '.' [digits] | ['.'] digits
exponent-part  ::=  indicator [sign] digits
infinity       ::=  'Infinity' | 'Inf'
nan            ::=  'NaN' [digits] | 'sNaN' [digits]
numeric-value  ::=  decimal-part [exponent-part] | infinity
numeric-string ::=  [sign] numeric-value | [sign] nan

The Decimal class provides some mathematical operations such as sqrt and log . However, it doesn't have all the functions defined in the math module. 
When you use functions from the math module for decimal numbers, Python will cast the Decimal objects to floats before carrying arithmetic operations.
'''

'https://www.geeksforgeeks.org/decimal-functions-python-set-1/'

# importing "decimal" module to use decimal functions
import decimal
 
# using as_tuple() to return decimal number as tuple
a = decimal.Decimal(-4.5).as_tuple()
 
# using fma() to compute fused multiply and addition
b = decimal.Decimal(5).fma(2,3)
 
# printing the tuple
print ("The tuple form of decimal number is : ", end="")
print (a)
 
# printing the fused multiple and addition
print ("The fused multiply and addition of decimal number is : ", end="")
print (b)

