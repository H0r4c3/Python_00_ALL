'https://www.geeksforgeeks.org/python-k-length-consecutive-characters/'

# Python3 code to demonstrate working of 
# K length consecutive characters
# Using split() + enumerate()
  
# initializing string
my_string = 'geekforgeeekssss is bbbbest forrrr geeks'
  
# printing original string
print(f'The original string is : {my_string}')
  
# initializing K 
K = 4
  
result = list()
for idx, char in enumerate(my_string):
    # creating equi string 
    substr = char * K
      
    # checking if equal to actual string 
    if my_string[idx : idx + K] == substr:
        result.append(substr)
      
# printing result 
print(f'The K length similar characters : {result}') 