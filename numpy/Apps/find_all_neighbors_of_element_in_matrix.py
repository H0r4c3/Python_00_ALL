'''
Having a matrix, find all the neighbors of an element in matrix
'''

import numpy as np

def find_coordinates(matrix, element):
    coordinates_element = np.where(matrix == element)
    x, y = coordinates_element[0], coordinates_element[1]
    coords_elem = [(x, y) for x, y in zip(coordinates_element[0], coordinates_element[1])]
    
    return coords_elem
    

def find_neighbors_(matrix, element):
    neighbors = list()
    coords_elem = find_coordinates(matrix, element)
    print(coords_elem)
    
    x, y = coords_elem[0][0], coords_elem[0][1]
     
    c1 = (x+1, y)
    c2 = (x, y+1)
    c3 = (x-1, y)
    c4 = (x, y-1)
    #print(c1, c2, c3, c4)
    
    if c1[0] >= 0 and c1[1] >= 0:
        neighbors.append(c1)
    if c2[0] >= 0 and c2[1] >= 0:
        neighbors.append(c2)
    if c3[0] >= 0 and c3[1] >= 0:
        neighbors.append(c3)
    if c4[0] >= 0 and c4[1] >= 0:
        neighbors.append(c4)
        
    return neighbors

def find_neighbors(matrix, element_coordinates):
    '''Find the <neighbors_coordinates> of neighbors for an element having <element_coordinates> in a <matrix>'''
    neighbors_coordinates = list()
    dimensions = matrix.shape
    
    x, y = element_coordinates[0], element_coordinates[0]
     
    c1 = (x+1, y) if x+1 <= dimensions[0] - 1 else None
    c2 = (x, y+1) if y+1 <= dimensions[1] - 1 else None
    c3 = (x-1, y) if x-1 >= 0 else None
    c4 = (x, y-1) if y-1 >= 0 else None
    print(c1, c2, c3, c4)
    
    neighbors_coordinates = [item for item in [c1, c2, c3, c4] if item != None]
    
    print(neighbors_coordinates)    
    return neighbors_coordinates


if __name__ == '__main__':
    my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    my_matrix = np.array(my_list)
    print(my_matrix)

    element_coordinates = (2, 2)
    neighbors_coordinates = find_neighbors(my_matrix, element_coordinates)
    print(neighbors_coordinates)
