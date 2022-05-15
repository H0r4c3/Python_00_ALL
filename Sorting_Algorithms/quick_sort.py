'https://www.udemy.com/course/sorting-and-searching-algorithms-python/learn/lecture/29684344#overview'


'''
Dividing the input list is referred to as partitioning the list. 
Quicksort first selects a pivot element and partitions the list around the pivot, putting every smaller element into a low array and 
every larger element into a high array.

Putting every element from the low list to the left of the pivot and every element from the high list to the right positions the 
pivot precisely where it needs to be in the final sorted list. This means that the function can now recursively apply the same procedure to low and 
then high until the entire list is sorted.
'''

from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

import timeit

if __name__ == "__main__":
    #ARRAY_LENGTH = 10
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 10
    #array = [randint(0, 10) for i in range(10)]
    #print(array)

    array = [1, 8, 9, 5, 5, 1, 3, 10, 1, 7]
    result = quicksort(array)
    print(result)
    
    # time for 50.000 calculations
    my_time = timeit.timeit("quicksort(array)", number = 50_000, globals = globals())
    print(f'bubble_sort(array) repeated 50_000 times = {my_time} seconds')