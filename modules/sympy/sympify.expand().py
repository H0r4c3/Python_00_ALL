'https://docs.sympy.org/latest/tutorial/simplification.html'

'''
expand() is one of the most common simplification functions in SymPy. 
Although it has a lot of scopes, for now, we will consider its function in expanding polynomial expressions.
'''

from sympy import sympify
string_1 = '(x-1)*(x+1)'

string_1 = sympify(string_1)
print(string_1)

string_1_expanded = string_1.expand()
print(string_1_expanded)

string_2 = str(string_1_expanded).replace(' ', '')
print(string_2)