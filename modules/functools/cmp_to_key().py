'https://docs.python.org/3/library/functools.html'
'https://www.educative.io/edpresso/what-is-functoolscmptokey-in-python'
'https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/'

'''
Transform an old-style comparison function to a key function. 
Used with tools that accept key functions (such as sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby()). 

The function takes a callable as a parameter.

cmp_to_key() uses a key to compare elements
It is built into functools module, thus functools has to be imported first in order to use the function
Used with tools that accept key functions such as min(), max(), sorted() etc.
Takes only one argument which strictly should be a callable
This function returns a special key that can be used to compare elements

functools.cmp_to_key(callable)
'''


from functools import cmp_to_key


def compare(x, y):
    if x == y: 
        return 0
    elif x > y:
        return 1
    else:
        return -1

    
my_list = [1, 4, 3, 5, 6, 7, 2]
print("List before sorting - ", my_list)

# my_list is sorted using the sort() method, passing the compare function as the parameter to cmp_to_key
my_list.sort(key=cmp_to_key(compare))
print("List after sorting - ", my_list)