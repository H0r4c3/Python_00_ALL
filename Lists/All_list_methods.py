'https://www.udemy.com/course/python-for-beginners-course-in-depth/learn/lecture/22315924#overview'

# 1. append() = Adds an element at the end of the list
print('# 1.')
my_list = [1, 2, 3, 4, 5]
my_list.append('H')
print(my_list)

# 2. clear() = Removes all elements from the list
print('# 2.')
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)

# 3. copy() = Returns a copy of the list
print('# 3.')
my_list = [1, 2, 3, 4, 5]
my_list2 = my_list.copy()
print(my_list2)

# 4. count() = Returns the number of elements with the specified value
print('# 4.')
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(my_list.count(3))

# 5. extend() = Adds the elements of a list (or any iterable), to the end of the current list
print('# 5.')
my_list = [1, 2, 3, 4, 5]
my_list2 = [11, 22, 33, 44, 55]
my_list.extend(my_list2)
print(my_list)

# 6. index() = Returns the index of the first element with the specified value
print('# 6.')
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))

# 7. insert() = Adds an element at the specified position
print('# 7.')
my_list = [1, 2, 3, 4, 5]
my_list.insert(3, 'H')
print(my_list)


# 8. pop() = Removes the element at the specified position
print('# 8.')
my_list = [1, 2, 3, 4, 5]
my_list.pop(0)
print(my_list)


# 9. remove() = Removes the FIRST item with the specified value
print('# 9.')
my_list = [1, 2, 3, 4, 5, 4]
my_list.remove(4)
print(my_list)

# 10. reverse() = Reverses the order of the list
print('# 10.')
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


# 11. sort() = Sorts the list
print('# 11.')
my_list = [5, 3, 4, 2, 1]
my_list.sort()
print(my_list)