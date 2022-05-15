'https://docs.python.org/3/library/heapq.html#module-heapq'

'''
heapq.heapify(iterable)
Transform 'iterable' into a heap, in-place, in linear time.

'''

import heapq
  
# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify() to convert list into heap
heapq.heapify(li)
  
# printing created heap
print (f'The created heap is : {list(li)}', end = "")