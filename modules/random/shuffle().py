'https://www.w3schools.com/python/ref_random_shuffle.asp'

'''
Shuffle a list (reorganize the order of the list items)

The shuffle() method takes a sequence, like a list, and reorganize the order of the items.

Note: This method changes the original list, it does not return a new list.

Syntax
random.shuffle(sequence, function)

sequence	Required. A sequence.
function	Optional. The name of a function that returns a number between 0.0 and 1.0. If not specified, the function random() will be used.
'''

import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)



def myfunction():
  return 0.1

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist, myfunction)

print(mylist)