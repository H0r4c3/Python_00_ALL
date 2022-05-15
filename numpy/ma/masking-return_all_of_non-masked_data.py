'https://py.checkio.org/en/mission/cipher-map2/'

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