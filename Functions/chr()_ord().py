'''
The Python chr() function is a built-in Python function that returns the string representing a character whose Unicode is an integer. 
Sometimes we need to convert an ASCII character to its corresponding character and for such cases Python chr() function is used.
The ord() method in Python converts a character into its Unicode code value.
'''

#print("The ASCII value of '" + c + "' is ", ord(c))
#print("The char with the ASCII value '" + 'a' + "' is ", chr(a))

for i in range(255):
    print(i, ' = ', chr(i))


my_list = ['a', 'A', 'Ă', 'Â', 'S', 'Ş', 'T', 'Ţ']

for item in my_list:
    print(item, ' = ', ord(item))