'''
Verify an 2D numpy array that fulfill the conditions for SUDOKU
'''

import numpy as np
import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\numpy\Apps\verify_sudoku.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')


def split_the_grid_in_small_squares(grid_arr):
    '''
    Split the grid in small squares and make a list with them
    '''
    ss_list = list()
    
    #ss0 = grid_arr[0:3, 0:3]
    #logging.debug(f'\n{ss0}')
    #ss1 = grid_arr[0:3, 3:6]
    #logging.debug(f'\n{ss1}')
    #ss2 = grid_arr[0:3, 6:9]
    #logging.debug(f'\n{ss2}')
    #ss3 = grid_arr[3:6, 0:3]
    #logging.debug(f'\n{ss3}')
    
    for m in range(0,9,3):
        for n in range(0,9,3):
            ss = grid_arr[m:m+3, n:n+3]
            print(ss)
            #logging.debug(f'\n{ss}')
            ss_list.append(ss)
            
    return ss_list


def verify_solution(grid_arr):
    
    NINE = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    logging.info(f'The grid for verification is: \n{grid_arr}')
    
    # verify the rows
    for r in range(9):
        logging.info(f'Verifying row nr. {r}: {grid_arr[r, :]}')
        if (np.sort(grid_arr[r, :]) == NINE).all():
            logging.debug(f'Row nr. {r} PASSED the verification!')
        else:
            logging.debug(f'Row nr. {r} FAILED the verification!')
            return False
            
    # verify the columns
    for c in range(9):
        logging.info(f'Verifying column nr. {c}: {grid_arr[:, c]}')
        if (np.sort(grid_arr[:, c]) == NINE).all():
            logging.debug(f'Column nr. {c} PASSED the verification!')
        else:
            logging.debug(f'Column nr. {c} FAILED the verification!')
            return False
    
    # verify the small squares
    ss_list = split_the_grid_in_small_squares(grid_arr)
    
    for nr_ss in range(9):
        logging.info(f'Verifying small square nr. {nr_ss}: \n{ss_list[nr_ss]}')
        ss = ss_list[nr_ss]
        ss_flat = ss.flatten()
        if (np.sort(ss_flat) == NINE).all():
            logging.debug(f'Small square nr. {nr_ss} PASSED the verification!')
        else:
            logging.debug(f'Small square nr. {nr_ss} FAILED the verification!')
            return False
    
    return True

my_list =  [[3, 7, 1, 6, 8, 4, 9, 5, 2],
            [8, 4, 9, 7, 2, 5, 3, 6, 1],
            [5, 6, 2, 9, 3, 1, 4, 7, 8],
            [6, 8, 7, 2, 1, 9, 5, 3, 4],
            [9, 1, 4, 3, 5, 7, 2, 8, 6],
            [2, 5, 3, 8, 4, 6, 1, 9, 7],
            [1, 3, 6, 5, 7, 2, 8, 4, 9],
            [4, 9, 8, 1, 6, 3, 7, 2, 5],
            [7, 2, 5, 4, 9, 8, 6, 1, 3]]


grid_arr = np.array(my_list)

result = verify_solution(grid_arr)

if result:
    logging.debug(f'The result of the verification: TRUE, the grid is SUDOKU!')
    print(f'The result of the verification: TRUE, the grid is SUDOKU!')
else:
    logging.debug(f'The result of the verification: FALSE, the grid is NOT SUDOKU!')
    print(f'The result of the verification: FALSE, the grid is NOT SUDOKU!')
