'''
Created on Oct 18, 2020

@author: Horace.000
'''
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # use max to make sure step can't go below 0
        step = max(0, step - 1) # the biggest argument gets returned
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

plt.hist(random_walk)
plt.show()