'''
https://www.hackerrank.com/challenges/string-validators/problem

Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
'''

# 1. str.isalnum() - This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
print('ab123'.isalnum())

# 2. str.isalpha() - This method checks if all the characters of a string are alphabetical (a-z and A-Z).
print('abcD'.isalpha())

# 3. str.isdigit() - This method checks if all the characters of a string are digits (0-9).
print('1234'.isdigit())

# 4. str.islower() - This method checks if all the characters of a string are lowercase characters (a-z).
print('abcd123#'.islower())

# 5. str.isupper() - This method checks if all the characters of a string are uppercase characters (A-Z).
print('ABCD123#'.isupper())