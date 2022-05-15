'https://www.w3schools.com/python/python_howto_remove_duplicates.asp'


# Method 1

mylist = ["a", "b", "a", "c", "c"]

# create a dictionary having as keys the items from mylist and as values None
print(dict.fromkeys(mylist))

mylist = list(dict.fromkeys(mylist))
print(mylist)


# Method 2
# transform the list in a set and, back, into list
mylist = ["a", "b", "a", "c", "c"]

myset = set(mylist)
mylist = list(myset)
print(mylist)

