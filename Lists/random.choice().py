'Choose a random item from a sequence. Here, sequence can be a list, tuple, string, or any iterable, like range.'

'''
random.choice(list)	 Choose a random item from a sequence. Here seq can be a list, tuple, string, or any iterable like range.
random.choices(list, k=3)	Choose multiple random items from a list, set, or any data structure.
random.choice(range(10, 101))	Pick a single random number from range 1 to 100
random.getrandbits(1)	Returns a random boolean
random.choice(list(dict1))	Choose a random key from a dictioanry
np.random.choice()	Return random choice from a multidimensional array
secrets.choice(list1)	Choose a random item from the list securely functions to generate random choice
'''

import random

my_list = ['One', 'Two', 'Three', 'Four', 'Five']
my_random_choice = random.choice(my_list)
print(my_random_choice)

my_random_choices = random.choices(my_list, k=3)
print(my_random_choices)

for i in range(10):
    my_random_choices = random.choices(my_list, k=3)
    print(my_random_choices)
