'https://scipython.com/book/chapter-6-numpy/examples/creating-a-magic-square/'

'''
A magic square is an N×N grid of numbers in which the entries in each row, column and main diagonal sum to the same number (equal to N(N2+1)/2). 
A method for constructing a magic square for odd N is as follows:

Step 1. Start in the middle of the top row, and let n=1;

Step 2. Insert n into the current grid position;

Step 3. If n=N2 the grid is complete so stop. Otherwise increment n;

Step 4. Move diagonally up and right, wrapping to the first column or last row if the move leads outside the grid. 
If this cell is already filled, move vertically down one space instead;

Step 5. Return to step 2.
'''

# Create an N x N magic square. N must be odd.
import numpy as np

N  = 5
magic_square = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2

while n <= N**2:
    magic_square[i, j] = n
    n += 1
    newi, newj = (i-1) % N, (j+1)% N
    if magic_square[newi, newj]:
        i += 1
    else:
        i, j = newi, newj

print(magic_square)