
import tkinter as tk
import logging
import config
from crossword_grid import CrosswordGrid
from crossword_solver import CrosswordSolver


log_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\Crossword_with_Modules\crossword_log.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=log_path, 
                    filemode='w')

logger = logging.getLogger('main')

#fill the crossword grid with the words from the result
def fill_the_crossword_grid(cells_arr, rows, columns):
    for i in range(rows):
        for j in range(columns):
            cells_arr[i][j].delete(0, tk.END)
            cells_arr[i][j].insert(0, config.result[i][j])
            

def main():
    #result = list()
    #my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\Crossword_Modules\words.txt'
    logging.info('Starting "main" method')
    
    #config.crossword = ['...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...', 'XX...X.XX', 'XX.XXX.X.', 'X......X.', 'XX.X.XXX.', 'XXXX.....']
    config.crossword = ['.XXX.', '...X.', '.X.X.', '.....']
    #config.crossword = ['.....', '.....', '.....', '.....', '.....']
    #config.crossword = ['......', '......', '......', '......', '......', '......']
    #config.crossword = ['...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...', 'XX...X.XX', 'XX.XXX.X.', 'X......X.', 'XX.X.XXX.', 'XXXX.....', '...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...']
    
    logging.info(f'config.crossword = {config.crossword}')
    #list_of_words = CrosswordSolver.read_words_from_file(config.my_path)
    #print(list_of_words)
    
    # Create the entire GUI program
    my_grid = CrosswordGrid(config.crossword)
    #solver = CrosswordSolver(crossword, list_of_words)
    
    my_grid.rows, my_grid.columns, my_grid.crossword_arr = my_grid.grid_dimensions()
    print(f'crossword_arr = {my_grid.crossword_arr}')
    print(f'rows = {my_grid.rows}')
    print(f'columns = {my_grid.columns}')
    
    logging.info(f'crossword_arr = {my_grid.crossword_arr}')
    logging.info(f'rows = {my_grid.rows}')
    logging.info(f'columns = {my_grid.columns}')
    
    # result_solve = solver.solve()
    # print(f'solver.solve() = {result_solve}')
    # config.result = solver.tolist()
    # print(f'result = {config.result}')
    
    # Fill the crossword grid with the words from the result
    #fill_the_crossword_grid(my_grid.cells_arr, my_grid.rows, my_grid.columns)
    
    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_grid.window.mainloop()
    
    return config.result
    
    
if __name__ == "__main__":
    main()