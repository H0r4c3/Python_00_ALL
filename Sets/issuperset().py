'https://www.programiz.com/python-programming/methods/set/issuperset'


'''
The issuperset() method returns True if a set has every elements of another set (passed as an argument). If not, it returns False.

Set A is said to be the superset of set B if all elements of B are in A.

A.issuperset(B)
'''

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))