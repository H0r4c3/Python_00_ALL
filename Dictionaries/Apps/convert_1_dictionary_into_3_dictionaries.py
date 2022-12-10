
def convert_dict_into_three_dicts(my_dict):
    '''
    Having a dictionary with keys = tuples, convert it into 2 types of dictionaries:
    - 1. dictionary type having as keys all the equal first elements of tuples and as values a list of values for those keys in the old dict
    - 2. dictionary type having as keys all the equal second elements of tuples and as values a list of values for those keys in the old dict
    - 3. dictionary type having as values the lists from small squares
    '''
    
    # analyzing the possible digits in every row
    dict_rows_0 = {0 : [value for key, value in my_dict.items() if key[0] == 0]}
    dict_rows_1 = {1 : [value for key, value in my_dict.items() if key[0] == 1]}
    dict_rows_2 = {2 : [value for key, value in my_dict.items() if key[0] == 2]}
    dict_rows_3 = {3 : [value for key, value in my_dict.items() if key[0] == 3]}
    dict_rows_4 = {4 : [value for key, value in my_dict.items() if key[0] == 4]}
    dict_rows_5 = {5 : [value for key, value in my_dict.items() if key[0] == 5]}
    dict_rows_6 = {6 : [value for key, value in my_dict.items() if key[0] == 6]}
    dict_rows_7 = {7 : [value for key, value in my_dict.items() if key[0] == 7]}
    dict_rows_8 = {8 : [value for key, value in my_dict.items() if key[0] == 8]}
    #dict_rows_8 = {key[0] : [value for key, value in my_dict.items() if key[0] == 8] for key in my_dict.keys() if key[0] == 8}
    list_dicts_rows = [dict_rows_0, dict_rows_1, dict_rows_2, dict_rows_3, dict_rows_4, dict_rows_5, dict_rows_6, dict_rows_7, dict_rows_8]
    

    # analyzing the possible digits in every column
    dict_cols_0 = {0 : [value for key, value in my_dict.items() if key[1] == 0]}
    dict_cols_1 = {1 : [value for key, value in my_dict.items() if key[1] == 1]}
    dict_cols_2 = {2 : [value for key, value in my_dict.items() if key[1] == 2]}
    dict_cols_3 = {3 : [value for key, value in my_dict.items() if key[1] == 3]}
    dict_cols_4 = {4 : [value for key, value in my_dict.items() if key[1] == 4]}
    dict_cols_5 = {5 : [value for key, value in my_dict.items() if key[1] == 5]}
    dict_cols_6 = {6 : [value for key, value in my_dict.items() if key[1] == 6]}
    dict_cols_7 = {7 : [value for key, value in my_dict.items() if key[1] == 7]}
    dict_cols_8 = {8 : [value for key, value in my_dict.items() if key[1] == 8]}
    #dict_cols_8 = {key[1] : [value for key, value in my_dict.items() if key[1] == 8] for key in my_dict.keys() if key[1] == 8}
    list_dicts_cols = [dict_cols_0, dict_cols_1, dict_cols_2, dict_cols_3, dict_cols_4, dict_cols_5, dict_cols_6, dict_cols_7, dict_cols_8]

    # analyzing the possible digits in every small square
    dict_small_square_0 = {0 : [value for key, value in my_dict.items() if key in [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]]}
    dict_small_square_1 = {1 : [value for key, value in my_dict.items() if key in [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]]}
    dict_small_square_2 = {2 : [value for key, value in my_dict.items() if key in [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]]}
    dict_small_square_3 = {3 : [value for key, value in my_dict.items() if key in [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)]]}
    dict_small_square_4 = {4 : [value for key, value in my_dict.items() if key in [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]]}
    dict_small_square_5 = {5 : [value for key, value in my_dict.items() if key in [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]]}
    dict_small_square_6 = {6 : [value for key, value in my_dict.items() if key in [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)]]}
    dict_small_square_7 = {7 : [value for key, value in my_dict.items() if key in [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]]}
    dict_small_square_8 = {8 : [value for key, value in my_dict.items() if key in [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]]}
    list_dicts_small_squares = [dict_small_square_0, dict_small_square_1, dict_small_square_2, dict_small_square_3, dict_small_square_4, 
                                dict_small_square_5, dict_small_square_6, dict_small_square_7, dict_small_square_8]
    
    return list_dicts_rows, list_dicts_cols, list_dicts_small_squares


my_dict = {(0, 0): [3], (0, 1): 7, (0, 2): 1, (0, 3): 6, (0, 4): 8, (0, 5): 4, (0, 6): 9, (0, 7): 5, (0, 8): 2, 
           (1, 0): [6, 8], (1, 1): 4, (1, 2): 9, (1, 3): 7, (1, 4): [1, 2, 3, 5], (1, 5): [1, 2, 5], (1, 6): [3, 8], (1, 7): [6, 8], (1, 8): [1, 3, 6, 8], 
           (2, 0): 5, (2, 1): [2, 6], (2, 2): [2, 6, 8], (2, 3): [1, 2, 9], (2, 4): [1, 2, 3], (2, 5): [1, 2, 9], (2, 6): 4, (2, 7): 7, (2, 8): [1, 3, 6, 8], 
           (3, 0): [1, 6, 9], (3, 1): 8, (3, 2): 7, (3, 3): [1, 2, 9], (3, 4): [1, 2, 6], (3, 5): [1, 2, 6, 9], (3, 6): 5, (3, 7): 3, (3, 8): 4, 
           (4, 0): [1, 4, 6, 9], (4, 1): [1, 5, 6, 9], (4, 2): [4, 5, 6], (4, 3): 3, (4, 4): [1, 4, 5, 6], (4, 5): 7, (4, 6): 2, (4, 7): [6, 8], (4, 8): [6, 8], 
           (5, 0): 2, (5, 1): [5, 6], (5, 2): 3, (5, 3): 8, (5, 4): [4, 5, 6], (5, 5): [5, 6], (5, 6): 1, (5, 7): 9, (5, 8): 7, 
           (6, 0): [1, 6, 8], (6, 1): [1, 2, 3, 5, 6], (6, 2): [2, 5, 6, 8], (6, 3): [1, 2, 5], (6, 4): 7, (6, 5): [1, 2, 5, 6], (6, 6): [3, 8], (6, 7): 4, (6, 8): 9, 
           (7, 0): [1, 4, 6, 8, 9], (7, 1): [1, 5, 6, 9], (7, 2): [4, 5, 6, 8], (7, 3): [1, 5], (7, 4): [1, 5, 6], (7, 5): 3, (7, 6): 7, (7, 7): 2, (7, 8): [5, 8], 
           (8, 0): 7, (8, 1): [2, 3, 5], (8, 2): [2, 5], (8, 3): 4, (8, 4): 9, (8, 5): 8, (8, 6): 6, (8, 7): 1, (8, 8): [3, 5]}


list_dicts_rows, list_dicts_cols, list_dicts_small_squares = convert_dict_into_three_dicts(my_dict)

print(list_dicts_rows)
print(list_dicts_cols)
print(list_dicts_small_squares)