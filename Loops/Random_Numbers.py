'''
Created on Oct 18, 2020

@author: Horace.000
'''
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123) #same seed -> same random numbers

#print(np.random.rand())

coin = np.random.randint(0,2) #Randomly, generates 0 or 1
print(coin)

# heads or tails
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
        
print(outcomes)

# random steps converted into a random walk
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
    
print(tails) #the final element in the list "tails" tells how often tails was thrown


# random steps converted into a random walk
final_tails = []
for x in range(1000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
    
print(final_tails) # the number of tails that were thrown in a game of 10 tossed

plt.hist(final_tails, bins = 10)
plt.show()

        
