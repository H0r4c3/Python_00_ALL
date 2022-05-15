'''
https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/
The original string is : Geeks
All substrings of string are : [‘G’, ‘Ge’, ‘Gee’, ‘Geek’, ‘Geeks’, ‘e’, ‘ee’, ‘eek’, ‘eeks’, ‘e’, ‘ek’, ‘eks’, ‘k’, ‘ks’, ‘s’]
'''

# Method 1 : Using list comprehension + string slicing

# initializing string 
test_str = "2453"
test_str = '23623714'
K = int(6260)
  
# printing original string 
print("The original string is : " + str(test_str))
  
# Get all substrings of string
# Using list comprehension + string slicing
my_list = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]
  
# printing result 
print("All substrings of string are : " + str(my_list))



counter = 0  
for item in my_list:
    result = 1
    for x in item:
        result = result * x
        if int(result) <= int(K):
            counter = counter + 1
            result = 1
print('Counter = ', counter)





# Method 2 : Using itertools.combinations()
# This particular task can also be performed using the inbuilt function of combinations, which helps to get all the possible combinations

from itertools import combinations
  
# initializing string 
test_str = "123"
  
# printing original string 
print("The original string is : " + str(test_str))
  
# Get all substrings of string
# Using itertools.combinations()
my_list2 = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r = 2)]
  
# printing result 
print("All substrings of string are : " + str(my_list2))