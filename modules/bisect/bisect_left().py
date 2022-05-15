'https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/'

'''
The purpose of Bisect algorithm is to find a position in list where an element needs to be inserted to keep the list sorted.

Python in its definition provides the bisect algorithms using the module “bisect” which allows to keep the list in sorted order after insertion of each element. 
This is essential as this reduces overhead time required to sort the list again and again after insertion of each element.

Important Bisection Functions

1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain 
the resultant list in sorted order. If the element is already present in the list, the right most position where element has to be inserted is returned. 
This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to 
be considered.

2. bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain 
the resultant list in sorted order. If the element is already present in the list, the left most position where element has to be inserted is returned. 
This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position 
which has to be considered.

3. bisect_right(list, num, beg, end) :- This function works similar to the “bisect()” and mentioned above.
'''

# Python code to demonstrate the working of
# bisect(), bisect_left() and bisect_right()
  
# importing "bisect" for bisection operations
import bisect
  
# initializing list
li = [1, 5, 3, 9, 7, 13, 11]
  
# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect(li, 4))
  
# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print ("The leftmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_left(li, 4))
  
# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_right(li, 4, 0, 4))