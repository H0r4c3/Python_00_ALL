'https://www.geeksforgeeks.org/python-statistics-mode-function/'

'''
The mode of a set of data values is the value that appears most often. It is the value at which the data is most likely to be sampled. 
A mode of a continuous probability distribution is often considered to be any value x at which its probability density function has a local maximum value, 
so any peak is a mode.
Python is very robust when it comes to statistics and working with a set of a large range of values. 
The statistics module has a very large number of functions to work with very large data-sets. 
The mode() function is one of such methods. This function returns the robust measure of a central data point in a given range of data-sets.

Syntax :
mode([data-set])
Parameters : 
[data-set] which is a tuple, list or a iterator of 
real valued numbers as well as Strings.
Return type : 
Returns the most-common data point from discrete or nominal data.
Errors and Exceptions : 
Raises StatisticsError when data set is empty.

If there are multiple modes with the same frequency, returns the first one encountered in the data. 
If the smallest or largest of those is desired instead, use min(multimode(data)) or max(multimode(data)). 
If the input data is empty, StatisticsError is raised.
'''

# mode() function a sub-set of the statistics module
import statistics
 
# declaring a simple data-set consisting of real valued positive integers.
my_list =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]
 
# In the given data-set
# Count of 1 is 1
# Count of 2 is 1
# Count of 3 is 2
# Count of 4 is 3
# Count of 5 is 2
# Count of 6 is 1
# We can infer that 4 has the highest population distribution
# So mode of set1 is 4
 
# Printing out mode of given data-set
print(f'Mode of given data set is {(statistics.mode(my_list))}')

