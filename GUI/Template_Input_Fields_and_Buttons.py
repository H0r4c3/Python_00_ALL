import tkinter as tk
from tkinter import ttk
from tkinter import Frame

class All_User_Input_Widgets():
    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Horace")

        # declaring string variable for storing the input strings
        self.input1 = tk.StringVar()

        # methods for creating the field and the buttons
        self.create_input_fields()
        self.create_buttons()

    def create_input_fields(self):
        # creating a label for input field 1
        self.field1_label = ttk.Label(self.window, width=20, text = 'Input Field 1', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.window, width=50, textvariable = self.input1, font=('arial', 10, 'normal')) 

        # Placing the labels and entries in the required position using grid method 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

        self.field1_label.grid(row=0, column=0)
        self.field1_entry.grid(row=0, column=1)

    def submit(self): 
        text1 = self.input1.get() # the string entered in the input field 1
        print("Input text 1 : " + text1) 
        self.input1.set("") # empty the field after printing

    def create_buttons(self):
        # creating a button that will call the "submit" function
        self.submit_button=ttk.Button(self.window, text = 'Submit', command = self.submit) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.window, text = 'Quit', command = self.window.destroy)
    
        # Place the Buttons
        self.submit_button.grid(row=3, column=1) 

        self.quit_button.grid(row=3, column=10)


def main():

        # Create the entire GUI program
        my_GUI = All_User_Input_Widgets()

        # Start the GUI event loop (performing an infinite loop for the window to display)
        my_GUI.window.mainloop()

if __name__ == "__main__":
    main()
        
