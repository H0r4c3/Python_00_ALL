'https://www.pythonmorsels.com/topics/passing-functions-arguments-other-functions/'

fruits = ['kumquat', 'cherimoya', 'Cherimoya', 'Loquat', 'longan', 'jujube']

# sorted doesn't quite alphabetize this list because when Python sorts strings it puts all the uppercase letters before 
# all the lowercase letters (due to their ASCII/unicode ordering).
my_list1 = sorted(fruits)
print(my_list1)

# We can fix this, by supplying a key argument to the built-in sorted function.
help(sorted)
# -> sorted(iterable, /, *, key=None, reverse=False)

'''
This key argument should be a function that will be called with each of the individual items in our fruits iterable and it should return the thing to sort by.
In our case, we could make a function that lowercases any string given to it in order to sort by the lowercase versions of each string:
'''

def lowercase(string):
    return string.lower()

# To sort by lowercased strings, we'll call sorted with a key argument that points to this lowercase function:
# Notice that when we called sorted, we didn't put parentheses (()) after lowercase to call it
my_list2 = sorted(fruits, key=lowercase)
print(my_list2)


# 42 is considered 0 in sorting
my_list3 = sorted([8, 3, 2, 42, 5], key=lambda x: 0 if x==42 else x)
print(my_list3) # [42, 2, 3, 5, 8]


# sorted after the length of the items
my_list4 = ['one', 'four', 'seven', 'two', 'zero']
result = sorted(my_list4, key=len)
print(result)



