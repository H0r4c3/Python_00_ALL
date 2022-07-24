import numpy as np

my_list = [
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]]

my_matrix = np.array(my_list)

#print(my_matrix)

print('Rows: \n')
for row in my_matrix:
    print(row)
    
print('\n')

print('Columns: \n')    
for i in range(4):
    print(my_matrix[:,i])