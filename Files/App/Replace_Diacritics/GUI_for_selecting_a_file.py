# Program with input fields + buttons + message box  
  
import os

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class CreateMenusFieldsButtons():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Replace the diacritics in a srt file (subtile file)")
        self.root.geometry('1300x100+400+400')
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Create some room around all the internal frames
        self.root['padx'] = 5
        self.root['pady'] = 5

        # declaring string variable for storing the input strings
        self.input_field = tk.StringVar() 

        self.path = 'Select File and press START'
        
        self.list_of_variables = []
        self.list_of_lines_file1 = []
        self.list_of_values = []

        self.create_frame_for_labels_and_entry_fields()
        self.menus()
        self.create_input_fields()
        self.position_input_fields()
        self.create_buttons()

    
    def create_frame_for_labels_and_entry_fields(self):
        self.frame1 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame2 = tk.Frame(self.root, relief=tk.RIDGE)

        # the fill keyword argument to specify in which direction the frames should fill
        # the side keyword argument of .pack() specifies on which side of the window the widget should be placed.
        self.frame1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5) 
        self.frame2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def create_input_fields(self):
        # creating a label for the input field
        self.field_label = ttk.Label(self.frame1, width=15, text = 'Path for the File:', font=('arial', 10, 'bold'))
        
        # creating an entry for the input field
        self.field_entry = ttk.Entry(self.frame1, width=100, textvariable = self.input_field, font=('arial', 10, 'normal')) 
        
        # default value for input field
        self.field_entry.insert(tk.END, self.path)

        # Placing the labels and entries in the required position using one of the 3 methods: 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

    def position_input_fields(self):
        self.field_label.pack(padx=1, pady=5, side=tk.LEFT)
        self.field_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X, expand=tk.YES)

    def menus(self):
        # Menus
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Select the file", command=self.browse_for_file)
        menubar.add_cascade(label="Select File", font=('arial', 10, 'bold'), menu=filemenu)
        self.root.config(menu=menubar)

    def create_buttons(self):
        # creating a button that will call the "method_for_button_START" method
        self.ok_button=ttk.Button(self.frame2, text = 'START', command = self.method_for_button_START)
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame2, text = 'Quit', command = self.root.destroy)

        self.ok_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)


    def method_for_button_START(self): 
        #Defining a function for button START
        
        from replace_diactritics_in_srt_file_with_GUI import ReplaceDiacriticsInSrtFile
        
        my_object = ReplaceDiacriticsInSrtFile()
        
        print(f'The path of the file is: {self.path}')
        
        try:
            input = self.input_field.get() # the string entered in the input field "Path for the File"
            self.path = input
            path1 = self.path
            path2 = str(path1).replace('.srt', '_NEW.srt')
    
            content = my_object.read_content_from_file(path1)
            content_without_diacritics = my_object.replace_chars(content)
            my_object.write_content_to_file(path2, content_without_diacritics)
            
        except FileNotFoundError as f:
            print(f)
            print('Select a srt file!')
            
        return self.path
        
        
    def browse_for_file(self):
        self.path = filedialog.askopenfilename()
        self.input_field.set("Select File and press START")
        self.field_entry.insert(tk.END, self.path)
        print("Selected file: ", self.path)

        #return self.path


# def main():
#     # Create the entire GUI program
#     my_GUI = CreateMenusFieldsButtons()

#     # Start the GUI event loop (performing an infinite loop for the window to display)
#     my_GUI.root.mainloop()


# if __name__ == "__main__":
#     main()
