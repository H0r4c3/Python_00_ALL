'https://www.geeksforgeeks.org/how-to-check-if-an-object-is-iterable-in-python/'

'''
We could verify that an object is iterable by checking whether it is an instance of the Iterable class.
'''


from collections.abc import Iterable
    
name = 'Roster'
  
if isinstance(name, Iterable):
  print(f"{name} is iterable")
    
else:
  print(f"{name} is not iterable")