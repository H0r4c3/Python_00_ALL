
from collections import deque
'https://appdividend.com/2021/06/18/how-to-prepend-to-list-in-python/'

'''
If you insert at the front of a list, python has to move all the other items one space forwards; lists can’t “make space at the front”. 
The collections.deque(double-ended queue) supports “making space at the front” and is much faster in this case.
'''


listA = [2, 3, 4]
print("Original list: ", listA)

listB = deque(listA)
listB.appendleft(1)
print("After prepending: ", list(listB))
