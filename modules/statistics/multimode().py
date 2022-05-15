'https://docs.python.org/3/library/statistics.html'

'''
statistics.multimode(data)

Return a list of the most frequently occurring values in the order they were first encountered in the data. 
Will return more than one result if there are multiple modes or an empty list if the data is empty:
'''

from statistics import multimode
my_string = 'aabbbbccddddeeffffgg'
print(multimode(my_string))
