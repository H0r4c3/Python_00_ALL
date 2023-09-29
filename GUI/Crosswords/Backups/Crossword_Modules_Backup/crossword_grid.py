import tkinter as tk
import numpy as np
from tkinter import ttk
from collections import defaultdict
from crossword_solver import CrosswordSolver

import config


my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\words.txt'

class CrosswordGrid:
    #global my_path
    
    def __init__(self, crossword):
        self.window = tk.Tk()
        self.window.title("Crossword")
        self.window.geometry('900x900+400+50')
        self.crossword = crossword
        self.cells_arr = np.empty(shape=(len(crossword), len(crossword[0])), dtype = tk.Entry) # array with cells (objects of class Entry)
        self.mask_dict = {} # dictionary with values from crossword
        
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # Declaring string variables for storing the input strings
        self.input_fields_arr = np.empty(shape=(len(crossword), len(crossword[0])), dtype = tk.StringVar)
        for i in range(len(crossword)):
            for j in range(len(crossword[0])):
                self.input_fields_arr[i][j] = tk.StringVar() 
                
        self.create_frames_for_labels_and_entry_fields_and_buttons()
        self.create_labels()
        self.create_cells()
        self.create_buttons()
        
        #self.list_of_words = CrosswordSolver.read_words_from_file(my_path)
        #self.dict_of_words = CrosswordSolver.convert_list_into_dict(self.list_of_words)

        
    def grid_dimensions(self):
        self.crossword = [list(item) for item in self.crossword]
        self.crossword_arr = np.array(self.crossword)
        
        self.rows = len(self.crossword_arr)
        self.columns = len(self.crossword_arr[0])
        
        return self.rows, self.columns, self.crossword_arr

    def create_frames_for_labels_and_entry_fields_and_buttons(self):
        self.frame_h = tk.Frame(self.window, relief=tk.RIDGE) # the frame for horizontal labels
        self.frame_v = tk.Frame(self.window, relief=tk.RIDGE) # the frame for vertical labels
        self.frame_c = tk.Frame(self.window, relief=tk.RIDGE) # the frame for cells in grid
        self.frame_b = tk.Frame(self.window, relief=tk.RIDGE) # the frame for buttons
        
        self.frame_h.grid(row=0, column=1)
        self.frame_v.grid(row=1, column=0)
        self.frame_c.grid(row=1, column=1)
        self.frame_b.grid(row=1, column=2)
        
    def create_labels(self):
        self.rows, self.columns, self.mask_arr = self.grid_dimensions()
        # horizontal labels
        for col in range(0, self.columns):
            cell_label_h = tk.Label(self.frame_h, width=10, text=col, font = ('arial', 9, 'bold'), bg='red', border=3)
            cell_label_h.grid(row=0, column=col)
            #self.cells_dict[(0, col)] = cell
        
        # vertical labels
        for row in range(0, self.rows):
            cell_label_v = tk.Label(self.frame_v, width=3, height=5, text=row, font = ('arial', 9, 'bold'), bg='yellow', border=1)
            cell_label_v.grid(row=row, column=0)
            #self.cells_dict[(row, 0)] = cell
    
    def create_cells(self):
        # cells objects from Entry class
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                cell = tk.Entry(self.frame_c, width=2, textvariable = self.input_fields_arr[row][col], justify=tk.CENTER, font=('Arial', 50))
                self.cells_arr[row][col] = cell
                self.mask_dict[(row, col)] = '.'
                cell.grid(row=row, column=col)
                if self.mask_arr[row][col] == 'X':
                    cell.insert(0, '$')
                    cell.configure(bg="black")
                    self.mask_dict[(row, col)] = '$'
                    
        print(f'self.mask_dict = {self.mask_dict}')
        
    def create_buttons(self):
        # creating a button that will fill the cells
        self.fill_button=tk.Button(self.frame_b, text = 'Fill', command = lambda: self.fill_the_grid())
        # creating a button that will fill the cells
        #self.fill_button=tk.Button(self.frame_b, text = 'Fill', command = lambda: self.fill_the_grid())
        # creating a button that will call the "quit" function  
        self.quit_button=tk.Button(self.frame_b, text = 'Quit', command = self.window.destroy)
        
        self.fill_button.pack(padx=5, pady=5, side=tk.RIGHT)
        
        self.quit_button.pack(padx=5, pady=5, side=tk.RIGHT)
        
    def fill_the_grid(self):
        '''
        mask_dict = dictionary having keys = coordinates, values = . or $
        cells_arr = array with cells (objects of class Entry)
        input_fields_arr = array with textvariables of type StringVar for reading what is written in cells (using get())
        '''
        
        #fill the crossword grid with the words from the result
        for i in range(self.rows):
            for j in range(self.columns):
                self.cells_arr[i][j].delete(0, tk.END)
                self.cells_arr[i][j].insert(0, config.result[i][j])
                
        

def main():
    print('For starting the program, you must use app.py!')


if __name__ == "__main__":
   main()