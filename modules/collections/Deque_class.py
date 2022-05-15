'https://appdividend.com/2021/06/18/how-to-prepend-to-list-in-python/'

from collections import deque

listA = [2, 3, 4]
print("Original list: ", listA)

listA = deque(listA)
listA.appendleft(1)
print("After prepending: ", list(listA))