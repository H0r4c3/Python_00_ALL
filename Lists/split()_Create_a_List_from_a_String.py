string1 = 'abcdef 12345'

list1 = string1.split() # default separator is the whitespace

list2 = string1.split('2') # default separator is 2

list3 = list(string1)

print(list1)
print(list2)
print(list3)