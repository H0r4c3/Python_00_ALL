'''
Solving a system of linear equations
https://stackabuse.com/solving-systems-of-linear-equations-with-pythons-numpy/
'''
import numpy as np

'''
4x + 3y + 2z = 25
-2x + 2y + 3z = -10
3x -5y + 2z = -4
'''

def solve_system_of_equations(a, b):
    
    a = np.array(a)
    b = np.array(b)
    solution = np.linalg.solve(a, b)
    
    print(solution)
    print(f'x = {int(solution[0])}')
    print(f'x = {int(solution[1])}')
    print(f'x = {int(solution[2])}')
    
    return solution

# 1.
a = [[4, 3, 2], [-2, 2, 3], [3, -5, 2]]
b = [25, -10, -4]

solution = solve_system_of_equations(a, b)

# 2.
a = [[1, 2, 3], [11, 12, 13], [21, 22, 23]]
b = [15, 15, 15]

solution = solve_system_of_equations(a, b)




