import time
import random

target = random.randint(2,4) # target seconds to wait
print('\nYour target time is {} seconds'.format(target))

input(' ---Press Enter to Begin--- ')
start = time.perf_counter()
    
input('\n...Press Enter again after {} seconds...'.format(target))
elapsed = time.perf_counter() - start
    
print('\nElapsed time: {0:.3f} seconds'.format(elapsed))