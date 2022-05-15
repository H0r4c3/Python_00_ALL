# Program with input fields + buttons + message box  
  
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tksheet

import os
from pathlib import Path

import pandas as pd

from create_a_sheet import CreateSheet

#path1 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/013998-03.hmf"
#path2 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/Test_Result03AB.html"
path3 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/What_to_check.txt"


class CreateMenusFieldsButtons():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Compare variables in two files")
        self.frame = tk.Frame(self.window, relief=tk.RIDGE)

        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        #self.input1 = tk.StringVar()
        #self.input2 = tk.StringVar()

        # declaring string variable for storing the input strings
        self.input_field1 = tk.StringVar() 
        self.input_field2 = tk.StringVar()

        self.path1 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/013998-03.hmf"
        self.path2 = 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/Test_Result03AB.html'
        
        self.list_of_variables = []
        self.list_of_lines_file1 = []
        self.list_of_values = []

        self.create_frame_for_labels_and_entry_fields()
        self.menus()
        self.create_input_fields()
        self.position_input_fields()
        self.create_buttons()

    
    def create_frame_for_labels_and_entry_fields(self):
        self.frame1 = tk.Frame(self.window, relief=tk.RIDGE)
        self.frame2 = tk.Frame(self.window, relief=tk.RIDGE)
        self.frame3 = tk.Frame(self.window, relief=tk.RIDGE)

        # the fill keyword argument to specify in which direction the frames should fill
        # the side keyword argument of .pack() specifies on which side of the window the widget should be placed.
        self.frame1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5) 
        self.frame2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.frame3.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def create_input_fields(self):
        # creating a label for input field 1
        self.field1_label = ttk.Label(self.frame1, width=15, text = 'Path for file 1', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.frame1, width=100, textvariable = self.input_field1, font=('arial', 10, 'normal')) 
        # default value for input field 1
        self.field1_entry.insert(tk.END, 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/013998-03.hmf')

        # creating a label for input field 1
        self.field2_label = ttk.Label(self.frame2, width=15, text = 'Path for file 2', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field2_entry = ttk.Entry(self.frame2, width=100, textvariable = self.input_field2, font=('arial', 10, 'normal')) 
        # default value for input field 1
        self.field2_entry.insert(tk.END, 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/File2.txt')

        # Placing the labels and entries in the required position using one of the 3 methods: 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

    def position_input_fields(self):
        self.field1_label.pack(padx=1, pady=5, side=tk.LEFT)
        self.field1_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)

        self.field2_label.pack(padx=1, pady=5, side=tk.LEFT)
        self.field2_entry.pack(padx=1, pady=5, side=tk.LEFT)


    def menus(self):
        # Menus
        menubar = tk.Menu(self.window)

        filemenu1 = tk.Menu(menubar, tearoff=0)
        filemenu2 = tk.Menu(menubar, tearoff=0)
        #filemenu.add_command(label="Select", command=filedialog.askdirectory)
        filemenu1.add_command(label="Select the file 1", command=self.browse_for_file1)
        filemenu2.add_command(label="Select the file 2", command=self.browse_for_file2)
        #filemenu.add_command(label="Save", command=filedialog.asksaveasfilename)
        #filemenu.add_separator()
        #filemenu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="Select File 1", menu=filemenu1)
        menubar.add_cascade(label="Select File 2", menu=filemenu2)

        self.window.config(menu=menubar)

    def create_buttons(self):

        # creating a button that will call the "method_for_button_COMPARE" method
        self.ok_button=ttk.Button(self.frame3, text = 'COMPARE', command = self.hmf_file) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame3, text = 'Quit', command = self.window.destroy)

        self.ok_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)


    def method_for_button_COMPARE(self): 
        """ Defining a function that will get the input text 1, input text 2, input text 3 and print them on the screen """
        #self.input1 = self.input_field1.get() # the string entered in the input field 1
        #self.input2 = self.input_field2.get() # the string entered in the input field 1
       
        #print("File 1 : " + self.input1) 
        #print("File 2 : " + self.input2)
        
        #self.input_field1.set("") 
       
        #self.input1_list = self.input1.split(',')
        
        # display the results in a sheet in window
        #self.sheet_object = CreateSheet(self)
        #self.sheet = self.sheet_object.create_a_sheet(self.input1_list)

        #self.window.state('zoomed')


    def browse_for_file1(self):
        self.path1 = filedialog.askdirectory()
        self.input_field1.set("")
        self.field1_entry.insert(tk.END, self.path1)
        #self.input1.set(self.path1)
        print("Selected file 1: ", self.path1)

        return self.path1

    def browse_for_file2(self):
        self.path2 = filedialog.askdirectory()
        self.input_field2.set("")
        self.field2_entry.insert(tk.END, self.path2)
        self.input2.set(self.path2)
        print("Selected file 2: ", self.path2)

        return self.path2

    def hmf_file(self):
        from check_values_in_two_files import FileWork

        file1_object = FileWork(self.path1) #HMF file
        file2_object = FileWork(self.path2) #Report file
        file3_object = FileWork(path3) #What_to_check.txt file (the variables for searching)

        print("Path1: ", self.path1)

        self.list_of_lines_file1 = file1_object.create_list_of_lines(self.path1)
        list_of_lines_file2 = file2_object.create_list_of_lines(self.path2)
        list_of_lines_file3 = file3_object.create_list_of_lines(path3)

        dict3 = file3_object.find_variable_and_value(list_of_lines_file3)
        self.list_of_variables = list(dict3.keys())

        dict1 = file1_object.find_variable_and_value(self.list_of_variables)
        self.list_of_values = list(dict1.values())
        print("List of values: ", self.list_of_values)

        df1 = pd.DataFrame.from_dict(dict1, orient = 'index', columns=['hmf_file'])
        print(df1)


        #display the results in a sheet in window
        self.sheet_object = CreateSheet(self)
        self.sheet = self.sheet_object.create_a_sheet()

        self.window.state('zoomed')

        df1.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/Comparison.xlsx', index = True)


def main():
    # Create the entire GUI program
    my_GUI = CreateMenusFieldsButtons()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()


if __name__ == "__main__":
    main()
