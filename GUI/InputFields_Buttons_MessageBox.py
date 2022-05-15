
# Program with input fields + buttons + message box  
  
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class All_User_Input_Widgets():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Horace")

        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # declaring string variable for storing the input strings
        self.input_field1 = tk.StringVar() 
        self.input_field2 = tk.StringVar() 
        self.input_field3 = tk.StringVar()

        self.create_input_fields()
        self.create_buttons()
   
 
    # Defining a function that will get the input text 1, input text 2, input text 3 and print them on the screen 
    def submit(self): 
  
        text1 = self.input_field1.get() # the string entered in the input field 1
        text2 = self.input_field2.get() # the string entered in the input field 2
        text3 = self.input_field3.get() # the string entered in the input field 3
      
        print("Input text 1 : " + text1) 
        print("Input text 2 : " + text2) 
        print("Input text 3 : " + text3)
      
        self.input_field1.set("") 
        self.input_field2.set("") 
        self.input_field3.set("")

      

    def create_input_fields(self):
        # creating a label for input field 1
        self.field1_label = ttk.Label(self.window, width=20, text = 'Input Field 1', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.window, width=50, textvariable = self.input_field1, font=('arial', 10, 'normal')) 
       
        # creating a label for input field 2
        self.field2_label = ttk.Label(self.window, width=20, text = 'Input Field 2', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 2
        self.field2_entry=ttk.Entry(self.window, width=50, textvariable = self.input_field2, font = ('arial', 10,'normal'))
    
        # creating a label for input field 3
        self.field3_label = ttk.Label(self.window, width=20, text = 'Input Field 3', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 3
        self.field3_entry=ttk.Entry(self.window, width=50, textvariable = self.input_field3, font = ('arial', 10,'normal'))

        # Placing the labels and entries in the required position using grid method 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

        self.field1_label.grid(row=0, column=0)
        self.field1_entry.grid(row=0, column=1) 

        self.field2_label.grid(row=1, column=0) 
        self.field2_entry.grid(row=1, column=1)

        self.field3_label.grid(row=2, column=0)
        self.field3_entry.grid(row=2, column=1)

  
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