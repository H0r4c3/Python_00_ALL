'https://www.geeksforgeeks.org/python-ways-to-rotate-a-list/'


# Method #1 : Using Slicing

my_list = [1, 2, 3, 4, 5]
  
# printing original list 
print ("Original list : " + str(my_list))
  
# using slicing to left rotate by 1
new_list = my_list[1:] + my_list[:1]
  
# Printing list after left rotate
print ("List after left rotate by 1 : " + str(new_list))

# using slicing to right rotate by 1
new_list = my_list[-1:] + my_list[:-1]
  
# Printing list after right rotate
print ("List after right rotate by 1 : " + str(new_list))



# Method #2 : Using list Comprehension

# printing original list 
print ("Original list : " + str(my_list))
  
# using list comprehension to left rotate by 3
new_list = [my_list[(i + 3) % len(my_list)] for i, x in enumerate(my_list)]
  
# Printing list after left rotate
print ("List after left rotate by 3 : " + str(new_list))
  
# using list comprehension to right rotate by 3
new_list = [my_list[(i - 3) % len(my_list)] for i, x in enumerate(my_list)]
  
# Printing after right rotate
print ("List after right rotate by 3: " + str(new_list))


# Method #3 : Using collections.deque.rotate()

from collections import deque

# printing original list 
print ("Original list : " + str(my_list))
  
# using rotate() to left rotate by 1
new_list_obj = deque(my_list)
new_list_obj.rotate(-1)
new_list = list(new_list_obj)
  
# Printing list after left rotate
print ("List after left rotate by 1 : " + str(new_list))
  
# using rotate() to right rotate by 1
new_list_obj = deque(my_list)
new_list_obj.rotate(1)
new_list = list(new_list_obj)
  
# Printing after right rotate
print ("List after right rotate by 1 : " + str(new_list))