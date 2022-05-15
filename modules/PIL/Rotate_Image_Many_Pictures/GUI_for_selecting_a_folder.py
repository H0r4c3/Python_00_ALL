# Program with input fields + buttons + message box  
  
import os

from all_files_from_a_folder import AllFilesFromAFolder
from rotate_image_many_pictures import RotateImageManyPictures

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from pathlib import Path

class GUIForSelectingAFolder():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Select a Folder to work with it")
        self.root.geometry('1300x100+400+400')
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Create some room around all the internal frames
        self.root['padx'] = 5
        self.root['pady'] = 5

        # declaring string variable for storing the input strings
        self.input_field = tk.StringVar() 

        # default value in the field
        self.path = r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\BACKUPs\Rotate_Image_Many_Pictures"
        
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
        self.field_label = ttk.Label(self.frame1, width=20, text = 'Path for the Folder:', font=('arial', 10, 'bold'))
        
        # creating an entry for the input field
        self.field_entry = ttk.Entry(self.frame1, width=100, textvariable = self.input_field, font=('arial', 10, 'normal')) 
        
        # default value for the input field
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
        filemenu.add_command(label="Select the folder", command=self.browse_for_folder)
        menubar.add_cascade(label="Select Folder", font=('arial', 10, 'bold'), menu=filemenu)
        self.root.config(menu=menubar)

    def create_buttons(self):
        # creating a button that will call the "method_for_button_START" method
        self.ok_button=ttk.Button(self.frame2, text = 'START', command = self.method_for_button_START) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame2, text = 'Quit', command = self.root.destroy)

        self.ok_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)


    def method_for_button_START(self): 
        input = self.input_field.get() # the string entered in the input field "Path for the Folder"
        #Defining a function for button START
        self.path = input
        print(f'The path of the folder is: {self.path}')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        
        my_object1 = AllFilesFromAFolder(self.path)
        folder_subfolder_files = my_object1.all_files_and_subfolders_in_a_folder()
        
        #print('folder_subfolder_files', folder_subfolder_files)
        
        list_of_path_of_files = my_object1.paths_of_files(folder_subfolder_files)
        
        #print('list_of_paths_of_files', list_of_path_of_files)
    
        list_of_paths_of_files_having_extension = my_object1.paths_of_files_having_specific_extension(list_of_path_of_files, ('.JPG', 'jpg'))
    
        #print('list_of_paths_of_files_having_extension', list_of_paths_of_files_having_extension)

        for pic in list_of_paths_of_files_having_extension:
            print(pic)
            
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        
        my_object2 = RotateImageManyPictures(list_of_paths_of_files_having_extension)

        my_object2.list_with_images_for_rotate = my_object2.create_list_with_images_for_rotate()

        number_of_rotated_pics = 0
        for path in my_object2.list_with_images_for_rotate:
            my_object2.rotate_image(path)
            number_of_rotated_pics +=1
            
        print(f"Rotated pictures: {number_of_rotated_pics}")
        
        return self.path
    

    def browse_for_folder(self):
        self.path = filedialog.askdirectory()
        self.input_field.set("")
        self.field_entry.insert(tk.END, self.path)
        print("Selected folder: ", self.path)

        #return self.path


# def main():
#     # Create the entire GUI program
#     my_GUI = GUIForSelectingAFolder()
#     path_folder = my_GUI.method_for_button_START()

#     # Start the GUI event loop (performing an infinite loop for the window to display)
#     my_GUI.root.mainloop()


# if __name__ == "__main__":
#     main()
