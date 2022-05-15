'https://www.w3schools.com/python/ref_keyword_assert.asp'

'''
The assert keyword is used when debugging code.
The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
You can write a message to be written if the code returns False
'''

# 1. Example

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"