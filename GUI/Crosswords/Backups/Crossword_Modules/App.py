
from crossword_grid import CrosswordGrid
from crossword_solver import CrosswordSolver

def main():
    my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\words.txt'
    #mask=['...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...', 'XX...X.XX', 'XX.XXX.X.', 'X......X.', 'XX.X.XXX.', 'XXXX.....']
    mask=['.XXX.', '...X.', '.X.X.', '.....']
    #mask=['...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...', 'XX...X.XX', 'XX.XXX.X.', 'X......X.', 'XX.X.XXX.', 'XXXX.....', '...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...']
    
    # Create the entire GUI program
    crossword = CrosswordGrid(mask)
    solver = CrosswordSolver()
    
    crossword.rows, crossword.columns, crossword.mask_arr = crossword.grid_dimensions()
    print(f'mask_arr = {crossword.mask_arr}')
    print(f'rows = {crossword.rows}')
    print(f'columns = {crossword.columns}')
    
    # crossword.create_frames_for_labels_and_entry_fields_and_buttons()
    # crossword.create_labels()
    # crossword.create_cells()
    # crossword.create_buttons()
    
    # Start the GUI event loop (performing an infinite loop for the window to display)
    crossword.window.mainloop()
    
    list_of_words = solver.read_words_from_file(my_path)
    
    # empty cells where we should put letters
    word_position, mask = solver.words_positions(mask)
    print(f'word_position = {word_position}')
    
    # words that fit in the space started there
    possib_words = solver.possible_words(word_position, mask, list_of_words)
    #print(f'possib_words = {possib_words}')
    
    decision, new_mask = solver.backtrack(mask, 0, word_position, possib_words)
    print(f'new_mask = {new_mask}')
    
    # if decision:
    #     # Return the filled crossword
    #     result = [''.join(row) for row in new_mask]
    #     print(result)
    #     return result
    # else:
    #     return []
    
    
    # Start the GUI event loop (performing an infinite loop for the window to display)
    crossword.window.mainloop()
    
    
if __name__ == "__main__":
    main()