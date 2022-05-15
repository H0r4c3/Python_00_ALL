'https://www.w3schools.com/python/ref_keyword_raise.asp'

'''
The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.
'''

# Examples:

# 1.

x = -1
x = 2 # comment this in order to obtain the Exception

if x < 0:
    raise Exception("Sorry, no numbers below zero")



# 2. Example -  Raise a TypeError if x is not an integer:

x = "hello"
x = 13 # comment this in order to obtain the Exception

if not type(x) is int:
  raise TypeError("Only integers are allowed")


# 3. Example 

a = 6
b = 0

#b = 3 # comment this in order to obtain the Exception

try:
    #do_something_in_app_that_breaks_easily()
    a / b
except ZeroDivisionError as error:
    raise