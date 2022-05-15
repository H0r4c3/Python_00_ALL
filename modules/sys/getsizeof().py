'https://www.geeksforgeeks.org/difference-between-__sizeof__-and-getsizeof-method-python/'

'''
getsizeof() method calls the __sizeof__() method o the object with an additional garbage collector overhead. 
Hence the size returned by the getsize() method will be more than that returned by the __sizeof()__ method. 
For example, the getsizeof() method returns 64 bytes for an empty list and then 8 bytes for every additional element.
'''

import sys

a =[1, 2]
b =[1, 2, 3, 4]
c =[1, 2, 3, 4]
d =[2, 3, 1, 4, 66, 54, 45, 89]

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))



# Now let’s look at the __sizeof__() method. It returns the size of the object without any overhead.

w =[1, 2]
x =[4, 5, 7, 9]
y =[2, 8, 6, 56, 45, 89, 88]
z =[54, 45, 12, 23, 24, 90, 20, 40]

print(w.__sizeof__())
print(x.__sizeof__())
print(y.__sizeof__())
print(z.__sizeof__())