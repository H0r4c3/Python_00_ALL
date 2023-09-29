'https://www.programiz.com/python-programming/methods/built-in/any'

'''
The any() function returns True if any element of an iterable is True. If not, it returns False.

any(iterable)

any() Return Value
The any() function returns a boolean value:
True if at least one element of an iterable is true
False if all elements are false or if an iterable is empty
'''

boolean_list = ['True', 'False', 'True']

# check if any element is true
result = any(boolean_list)
print(result)



# False, since iterable is empty
l = []
print(any(l))



# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))


# check if all items in a list are equal to a value named 'total'
my_list = [15, 15, 15]
total = 15

if any([item != 15 for item in my_list]):
    print(f'Sum {my_list} on rows NOK! Should be = {total}!')
else:
    print(f'Sum {my_list} on rows OK! total = {total}!')