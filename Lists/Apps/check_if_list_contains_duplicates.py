'https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/'

import timeit

my_list = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']

# Method 1
def checkIfDuplicates_1(my_list):
    ''' Check if given list contains any duplicates '''
    if len(my_list) == len(set(my_list)):
        return False
    else:
        return True


# Method 2
def checkIfDuplicates_2(my_list):
    ''' Check if given list contains any duplicates '''    
    for item in my_list:
        if my_list.count(item) > 1: # It returns the occurrence count of element in the list.
            return True
    return False

print(checkIfDuplicates_1(my_list))

print(checkIfDuplicates_2(my_list))

# time for 1.500.000 calculations
my_time1 = timeit.timeit("checkIfDuplicates_1(my_list)", number = 1_500_000, globals = globals())
print(f'Time 1 = {my_time1}')

my_time2 = timeit.timeit("checkIfDuplicates_2(my_list)", number = 1_500_000, globals = globals())
print(f'Time 2 = {my_time2}')
