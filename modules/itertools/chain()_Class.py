'https://www.geeksforgeeks.org/python-itertools-chain/'

'''
It is a function / Class that takes a series of iterables and returns one iterable. It groups all the iterables together and produces a single iterable as output. 
Its output cannot be used directly and thus explicitly converted into iterables. 
This function come under the category iterators terminating iterators.

'''

from itertools import chain

#Example 1

# a list of odd numbers
odd = [1, 3, 5, 7, 9]

# a list of even numbers
even = [2, 4, 6, 8, 10]

# chaining odd and even numbers
numbers = list(chain(odd, even))

print(numbers)


# Example2
res = list(chain('ABC', 'DEF', 'GHI', 'JKL'))
print(res)