'https://blog.finxter.com/the-quicksort-algorithm-in-one-line-python/?tl_inbound=1&tl_target_all=1&tl_form_type=1&tl_period_type=3&utm_source=newsletter&utm_medium=email&utm_campaign=finxter_weekly_merry_christmas_free_book_pdf_inside&utm_term=2021-12-24'

'''
Quicksort sorts a list by recursively dividing the big problem (sorting one big list) into smaller problems (sorting two smaller lists) and 
combining the solutions from the smaller problems in a way that solves the big problem.

In order to solve each smaller problem, the same strategy is used recursively: the smaller problems are divided into even smaller subproblems, 
solved separately, and combined. Because of this strategy, Quicksort belongs to the class of “Divide and Conquer” algorithms.

The main idea of Quicksort is to select a pivot element and then place all elements that are greater than or equal to the pivot element to the right 
and all elements that are smaller than the pivot element to the left.
'''

def quicksort(my_list):
    # recursion base case - empty list
    if not my_list:
        return []
    # first element is pivot
    pivot = my_list[0]
    # break up problem
    smaller = [x for x in my_list[1:] if x < pivot]
    greater = [x for x in my_list[1:] if x >= pivot]
    # recursively solve problem and recombine solutions
    return quicksort(smaller) + [pivot] + quicksort(greater)

print(quicksort([4, 4, 3, 2, 1, 8, 9]))
# [1, 2, 3, 4, 4, 8, 9]




# ONE-LINER
## The Data
unsorted = [33, 2, 3, 45, 6, 54, 33]
## The Quicksort One-Liner
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
 
## The Result
print(q(unsorted))