'https://www.w3schools.com/python/ref_random_choices.asp'

'''
The choices() method returns a list with the randomly selected element from the specified sequence.

You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

random.choices(sequence, weights=None, cum_weights=None, k=1)

sequence	Required. A sequence like a list, a tuple, a range of numbers etc.
weights	Optional. A list were you can weigh the possibility for each value. Default None
cum_weights	Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4]. Default None
k	Optional. An integer defining the length of the returned list
'''

import random

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14))
