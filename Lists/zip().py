'https://www.programiz.com/python-programming/methods/built-in/zip'

'''
The zip() function returns an iterator of tuples based on the iterable objects.
If we do not pass any parameter, zip() returns an empty iterator
If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.
'''
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

result = zip(number_list, str_list)
print(list(result))
result = zip(number_list, str_list)
print(dict(result))


# Unzipping the Value Using zip()
result = zip(number_list, str_list)
result_list = list(result)

nr, st =  zip(*result_list)
print('nr =', nr)
print('st =', st)