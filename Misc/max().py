'https://thepythonguru.com/python-builtin-functions/max/'

'''
The max() function returns the largest of the input values.

Its syntax is as follows:

max(iterable[, default=obj, key=func]) -> value

PARAMETER	       DESCRIPTION
iterable (required)	An iterable object like string, list, tuple etc.
default (optional)	The default value to return if the iterable is empty.
key (optional)	It refers to the single argument function to customize the sort order. The function is applied to each item on the iterable.

or

max(a,b,c, ...[, key=func]) -> value

PARAMETER	    DESCRIPTION
a, b, c ...	Items to compare
key (optional)	It refers to the single argument function to customize the sort order. The function is applied to each item on the iterable.
'''

print(max("abcDEF")) # find largest item in the string

print(max([2, 1, 4, 3])) # find largest item in the list

# find largest item in the dict
print(max({1: "one", 2: "two", 3: "three"}))


# Here is an example where we use key argument to make the string comparision case-insentive.
print(max("c", "b", "a", "Y", "Z", key=str.lower))


# The following is another example where we compare strings based on its length instead of their ASCII values.
print(max(("python", "lua", "ruby"), key=len))