'https://www.geeksforgeeks.org/reduce-in-python/'


'''
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the 
list elements mentioned in the sequence passed along.This function is defined in “functools” module.
At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
'''


# python code to demonstrate working of reduce()
 
# importing functools for reduce()
import functools
 
# initializing list
my_list = [1, 3, 5, 6, 2]
 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, my_list))
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, my_list))