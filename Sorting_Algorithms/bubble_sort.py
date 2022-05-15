'https://www.udemy.com/course/sorting-and-searching-algorithms-python/learn/lecture/29684356#overview'

'https://realpython.com/sorting-algorithms-python/'

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array


import timeit
from random import randint

if __name__ == "__main__":
    #ARRAY_LENGTH = 10
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 10
    #array = [randint(0, 10) for i in range(10)]
    #print(array)

    array = [1, 8, 9, 5, 5, 1, 3, 10, 1, 7]
    result = bubble_sort(array)
    print(result)
    
    # time for 500.000 calculations
    my_time = timeit.timeit("bubble_sort(array)", number = 500_000, globals = globals())
    print(f'bubble_sort(array) repeated 500_000 times = {my_time} seconds')