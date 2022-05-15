


'https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html'

'''
Mask an array where a condition is met.

Return a as an array masked where condition is True. Any masked values of a or condition are also masked in the output.

Parameters
conditionarray_like
Masking condition. When condition tests floating point values for equality, consider using masked_values instead.

a array_like
Array to mask.

copy bool
If True (default) make a copy of a in the result. If False modify a in place and return a view.

Returns
result MaskedArray
The result of masking a where condition is True.
'''

# 1. Example
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



# 3. Example
b = ['a', 'b', 'c', 'd']
mask = ma.masked_where(a == 1, b) # what to mask (not show)
print(mask)