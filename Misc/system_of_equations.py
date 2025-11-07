'''
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

def solve_system_of_equations():

    # Define the system of equations
    A = np.array([[1, 1], [1, -1]])
    b = np.array([5, 1])

    # Solve the system of equations using np.linalg.solve
    solution = np.linalg.solve(A, b)

    # Print the solution
    print(f'The solution is: {solution}')



# Method nr. 2:

''''
For simpler systems or symbolic solutions, you can use libraries like SymPy. 
Here's how you can solve a system of equations using SymPy:
'''

from sympy import symbols, Eq, solve

def solve_system_of_equations_(list_of_unknowns):
    # Define the symbols
    x, y = symbols('x y')

    # Define the equations
    eq1 = Eq(2*x + 3*y, 13)
    eq2 = Eq(4*x - 5*y, -7)

    # Solve the system of equations
    solution = solve((eq1, eq2), (x, y))

    # Print the solution
    print(f'The solution using Method 2 is: {solution}')






# Test a different system of eq:
from sympy import symbols, Eq, solve

def solve_system_of_equations_(list_of_unknowns):
    
    # Define the symbols
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')

    # Define the equations
    eq1 = Eq(x1 + x2, 2)
    eq2 = Eq(x2 + x3, 2)
    eq3 = Eq(x3 + x4, 2)
    eq4 = Eq(x4 + x5, 2)
    eq5 = Eq(x5 + x6, 2)
    eq6 = Eq(x6 + x7, 2)
    eq7 = Eq(x7 + x8, 2)
    eq8 = Eq(x8 + x9, 2)
    eq9 = Eq(x9 + x10, 2)
    eq10 = Eq(x10 + x1, 2)
    

    # Solve the system of equations
    solution = solve((eq1, eq2), (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))
    
    return solution

def solve_system_of_equations_():
    
    # Define the symbols
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')

    # Define the equations
    eq1 = Eq(x1 + x2 + x3 + x4 + x5 + x6, 6)
    eq2 = Eq(x2 + x3 + x4 + x5 + x6 + x7, 6)
    eq3 = Eq(x3 + x4 + x5 + x6 + x6 + x8, 6)
    eq4 = Eq(x4 + x5 + x6 + x7 + x8 + x9, 6)
    eq5 = Eq(x5 + x6 + x7 + x8 + x9 + x10, 6)
    eq6 = Eq(x6 + x7 + x8 + x9 + x10 + x1, 6)
    eq7 = Eq(x7 + x8 + x9 + x10 + x1 + x2, 6)
    eq8 = Eq(x8 + x9 + x10 + x1 + x2 + x3, 6)
    eq9 = Eq(x9 + x10 + x1 + x2 + x3 + x4, 6)
    eq10 = Eq(x10 + x1 + x2 + x3 + x4 + x5, 6)
    

    # Solve the system of equations
    solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10), (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))
    print(f'The test solution is: {solution}')
    
    return solution

solve_system_of_equations()

#list_of_unknowns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
#solution = solve_system_of_equations(list_of_unknowns)
#solution = solve_system_of_equations('x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10')
#print(f'The test solution is: {solution}')
    