'https://realpython.com/python-filter-function/?__s=z6fw8dy8hh2ghqd22iv6'

'''
filter(function, iterable)
The first argument to filter() is a function object, which means that you need to pass a function without calling it with a pair of parentheses.
The second argument, iterable, can hold any Python iterable, such as a list, tuple, or set. It can also hold generator and iterator objects.
To perform the filtering process, filter() applies function to every item of iterable in a loop. The result is an iterator that yields the values of iterable for which function returns a true value. 
The process doesn’t modify the original input iterable.
'''

numbers = [-2, -1, 0, 1, 2]

# Using a lambda function
positive_numbers = filter(lambda n: n > 0, numbers)
print(positive_numbers)

my_list1 = list(positive_numbers)
print(my_list1)


# Using a user-defined function
def is_positive(n):
    return n > 0

my_list2 = list(filter(is_positive, numbers))
print(my_list2)

# Generating a list with filter()
# list(filter(function, iterable))

# Generating a list with a list comprehension
# [item for item in iterable if function(item)]