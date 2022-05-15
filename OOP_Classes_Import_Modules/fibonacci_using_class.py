'https://realpython.com/fibonacci-sequence-python/?__s=z6fw8dy8hh2ghqd22iv6'

import timeit

class FibonacciSequence():
    def __init__(self):
        self.cache = []
        self.cache.append(0)
        self.cache.append(1)

    def __call__(self, i):
        newfibnum = 0

        # Check input is valid
        if isinstance(i, int) and i >= 0:
            # If i is base case of 0 or 1
            if i == 0 or i == 1:
                return self.cache[i]

            # If i is NOT stored in the cache already
            elif i >= len(self.cache):
                newfibnum = self.__call__(i-1) + self.__call__(i-2)
                self.cache.append(newfibnum)

            # Previous two values in cache calculates i
            else:
                newfibnum = self.cache[i-1]+self.cache[i-2]

            # Return the result of the fib sequence entered by the user
            return self.cache[i]

        # If input is not valid give error message
        else:
            raise ValueError("Invalid input, please enter a positive integer for i")

# Instantiate the FibonacciSequence class
new_seq = FibonacciSequence()
#print(new_seq(6))

starttime = timeit.default_timer()
print("The start time is :", starttime)
print(f'Result = {new_seq(100)}')
print("The end time is :", timeit.default_timer())
print("The time difference is :", timeit.default_timer() - starttime)