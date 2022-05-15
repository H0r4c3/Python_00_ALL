'https://www.programiz.com/python-programming/methods/dictionary/update'

'''
The update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.

Syntax of Dictionary update()
The syntax of update() is:

dict.update([other])
update() Parameters
The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).

If update() is called without passing parameters, the dictionary remains unchanged.

Return Value from update()
update() method updates the dictionary with elements from a dictionary object or an iterable object of key/value pairs.

It doesn't return any value (returns None).
'''


marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}

marks.update(internal_marks)


print(marks)

# Output: {'Physics': 67, 'Maths': 87, 'Practical': 48}



# Example 2: update() When Tuple is Passed

d = {'x': 2}

d.update(y = 3, z = 0)

print(d)