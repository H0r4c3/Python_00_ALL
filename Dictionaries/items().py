'https://www.programiz.com/python-programming/methods/dictionary/items'


'''
The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
'''

my_dict = {1 : 'value1', 2 : 'value2', 3 : 'value3'}
for key, value in my_dict.items():
    print(key, value)
    
print(my_dict.items())