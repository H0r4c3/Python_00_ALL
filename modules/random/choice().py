
'Returns a random element from the given sequence'

import random

my_list = [1, 2, 3, 4, 5, 6, 7]

rand = random.choice(my_list)
print(rand)

for i in range(10):
    rand = random.choice(my_list)
    print(rand)