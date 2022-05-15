# Program with input fields + buttons + message box  
  
import tkinter as tk
from tkinter import ttk
#from tkinter import filedialog
import tksheet

import pandas as pd

from create_a_sheet import CreateSheet

class CreateFieldsButtons():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("eztv")
        self.frame = tk.Frame(self.window, relief=tk.RIDGE)

        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # declaring string variable for storing the input strings
        self.input_field1 = tk.StringVar() 
        self.input_field2 = tk.StringVar() 
        self.input_field3 = tk.StringVar()

        #self.input1_list = []
        #self.input2_list = []
        #self.input3_list = []

        self.create_frame_for_labels_and_entry_fields()
        self.create_input_fields()
        self.position_input_fields()
        self.create_buttons()

    
    def create_frame_for_labels_and_entry_fields(self):
        self.frame = tk.Frame(self.window, relief=tk.RIDGE)

        # the fill keyword argument to specify in which direction the frames should fill
        # the side keyword argument of .pack() specifies on which side of the window the widget should be placed.
        self.frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5) 

    def create_input_fields(self):
        # creating a label for input field 1
        self.field1_label = ttk.Label(self.frame, width=13, text = 'Input Field 1', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.frame, width=50, textvariable = self.input_field1, font=('arial', 10, 'normal')) 
        # default value for input field 1
        self.field1_entry.insert(tk.END, 'Default value for Field 1')
       
        # creating a label for input field 2
        self.field2_label = ttk.Label(self.frame, width=10, text = 'Input Field 2', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 2
        self.field2_entry=ttk.Entry(self.frame, width=50, textvariable = self.input_field2, font = ('arial', 10,'normal'))
    
        # creating a label for input field 3
        self.field3_label = ttk.Label(self.frame, width=10, text = 'Input Field 3', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 3
        self.field3_entry=ttk.Entry(self.frame, width=50, textvariable = self.input_field3, font = ('arial', 10,'normal'))

        # Placing the labels and entries in the required position using one of the 3 methods: 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

    def position_input_fields(self):
        self.field1_label.pack(padx=5, pady=5, side=tk.LEFT)
        self.field1_entry.pack(padx=1, pady=5, side=tk.LEFT)


    def create_buttons(self):
        # creating a button that will call the "method_for_button_OK" method
        self.ok_button=ttk.Button(self.frame, text = 'OK', command = self.method_for_button_OK) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame, text = 'Quit', command = self.window.destroy)

        self.ok_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)


    def method_for_button_OK(self): 
        """ Defining a function that will get the input text 1, input text 2, input text 3 and print them on the screen """
        self.input1 = self.input_field1.get() # the string entered in the input field 1
        self.input2 = self.input_field2.get() # the string entered in the input field 2
        self.input3 = self.input_field3.get() # the string entered in the input field 3
      
        print("Input text 1 : " + self.input1) 
        print("Input text 2 : " + self.input2) 
        print("Input text 3 : " + self.input3)
      
        self.input_field1.set("") 
        self.input_field2.set("") 
        self.input_field3.set("")

        self.input1_list = self.input1.split(',')
        self.input2_list = self.input2.split(',')
        self.input3_list = self.input3.split(',')

        # display the results in a sheet in window
        self.sheet_object = CreateSheet(self)
        self.sheet = self.sheet_object.create_a_sheet(self.input1_list, self.input2_list, self.input3_list)

        #self.window.state('zoomed')


def main():
    # Create the entire GUI program
    my_GUI = CreateFieldsButtons()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()

    df = pd.DataFrame({"Field 1" : my_GUI.input1_list, "Field 2" : my_GUI.input2_list, "Field 3" : my_GUI.input3_list}, index=[0])

    # Converting to excel 
    df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/GUI/Templates_Classes/Output_Excel.xlsx', index = False)



if __name__ == "__main__":
    main()
