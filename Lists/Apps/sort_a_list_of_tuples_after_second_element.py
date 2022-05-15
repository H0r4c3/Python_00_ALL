'https://pythonguides.com/python-sort-list-of-tuples/'

'''
In python, if you want to sort a list of tuples by the second element then we have the function called sort() 
and by using lambda function as a key function. A custom comparator is a key function in sort().
'''

# sort list of tuples by second element
roll_list1 = [('Jack', 76), ('Beneth', 78), ('Cirus', 77), ('Faiz', 79)]
roll_list1.sort(key=lambda a: a[1])
print(roll_list1)


# sort list of tuples by first element, descending
roll_list1 = [('Jack', 76), ('Beneth', 78), ('Cirus', 77), ('Faiz', 79)]
roll_list1.sort(reverse=True)
print(roll_list1)