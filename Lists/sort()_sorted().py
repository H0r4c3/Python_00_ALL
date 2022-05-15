'''
sort() is a method that sorts the original list in place.
sorted() is a function that returns a sorted list. The original list remains unchanged.
'''

#1. sort()
my_list = [3, 1, 4, 5, 2]

my_list.sort()
print(my_list)

#2. sorted()
my_list = [3, 1, 4, 5, 2]

new_list = sorted(my_list)
print(my_list)
print(new_list)

#3. sorted() with key=
my_list = [['Monday', 25], ['Tuesday', 21], ['Wednesday', 30]]
sorted_list = sorted(my_list, key=lambda item: item[1]) # sorted after the second element from each list
print(sorted_list)
