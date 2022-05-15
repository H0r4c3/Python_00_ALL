'https://www.geeksforgeeks.org/python-convert-list-of-strings-and-characters-to-list-of-characters/'


# 1. Method #1 : Using List comprehension

# initializing list  
test_list = ['gfg', 'i', 's', 'be', 's', 't']
  
# printing original list
print ("The original list is : " + str(test_list))
  
# using list comprehension to convert list of string and characters to list of characters
res = [i for ele in test_list for i in ele]
  
# printing result 
print ("The list after conversion is : " +  str(res))


# 2. Method #2 : Using join()

res = list(''.join(test_list))
  
# printing result 
print ("The list after conversion is : " +  str(res))



# 3. Method #3 : Using chain.from_iterable()

from itertools import chain

res = list(chain.from_iterable(test_list))
  
# printing result 
print ("The list after conversion is : " +  str(res))