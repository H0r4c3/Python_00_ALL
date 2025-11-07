'''
2*x + 1*y = 5
1*x - 1*y = 1

2*x + 3*y = 13
4*x - 5*y = -7

x = 2
y = 3
'''

# Method nr. 1:

'''
In this example, A represents the coefficients matrix, and b represents the constants vector. 
The np.linalg.solve() function is then used to solve the system of equations represented by Ax = b. 
The solution is stored in the solution variable and printed out.

You can adjust the coefficients matrix A and the constants vector b according to your specific system of equations. 
This method works for systems of linear equations.
'''

import numpy as np

# Define the coefficients matrix (A) and the constants vector (b) for the system of equations
A = np.array([[2, 1], [1, -1]])
b = np.array([5, 1])

# Solve the system of equations
solution = np.linalg.solve(A, b)

# Print the solution
print("Solution:", solution)



# Method nr. 2:

''''
For simpler systems or symbolic solutions, you can use libraries like SymPy. 
Here's how you can solve a system of equations using SymPy:
'''

from sympy import symbols, Eq, solve

# Define the symbols
x, y = symbols('x y')

# Define the equations
eq1 = Eq(2*x + 1*y, 5)
eq2 = Eq(1*x - 1*y, 1)

# Solve the system of equations
solution = solve((eq1, eq2), (x, y))

# Print the solution
print(solution)