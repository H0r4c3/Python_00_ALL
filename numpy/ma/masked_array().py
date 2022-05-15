
'https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html'
'https://github.com/numpy/numpy/blob/v1.22.0/numpy/ma/core.py#L2703-L6224'

'''
numpy.ma.masked_array[source]

alias of numpy.ma.core.MaskedArray
'''


import numpy as np

def masking(grille, password):
    # creating the mask of grille_arr where condition grille_arr == 'X' is True
    mask = np.ma.masked_where(grille != 'X', grille)
    print(mask)

    # getting the mask of the array (False = where is NOT masked)
    result_mask = np.ma.getmask(mask)
    print(result_mask)

    # masking the array1 (password) with the result of mask of array2 (result_mask)
    masked = np.ma.masked_array(password, mask=result_mask)
    print(masked)

    # return all of non-masked data as a 1-D array
    masked_array = np.ma.compressed(masked)

    return masked_array

grille = ['X...', '..X.', 'X..X', '....']
grille_lists = list(map(list, grille))
grille_arr = np.array(grille_lists)

password = ['itdf', 'gdce', 'aton', 'qrdi']
pw_lists = list(map(list, password))
pw = np.array(pw_lists)
print(pw)
    
masked_array = masking(grille_arr, pw)
print(masked_array)



# 2. Example
import numpy.ma as ma
a = np.arange(4)
# array([0, 1, 2, 3])

mask = ma.masked_where(a <= 2, a) # what to mask (not show)
print(mask)
#masked_array(data=[--, --, --, 3], mask=[True, True, True, False], fill_value=999999)

result_mask = ma.getmask(mask)
print(result_mask)

# masking the array1 (a) with the result of mask of array2 (result_mask)
masked = np.ma.masked_array(a, mask=result_mask)
print(masked)



# 3. Example
b = ['a', 'b', 'c', 'd']
mask = ma.masked_where(a == 1, b) # what to mask (not show)
print(mask)

result_mask = ma.getmask(mask)
print(result_mask)

# masking the array1 with the result of mask of array2
masked = np.ma.masked_array(b, mask=result_mask)
print(masked)