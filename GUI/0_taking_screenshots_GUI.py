# Program with input fields + buttons + message box

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import time
import pyautogui


class CreateMenusFieldsButtons():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Taking Screenshots")
        self.window.geometry('1500x150+1000+800')
        self.style = ttk.Style()
        self.style.theme_use("default")

        # default path for screenshots
        self.path1 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\04_udemy_Courses\__udemy_Learn_Python_With_20+_Real_World_Projects__\screenshots'

        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # declaring string variable for storing the input strings
        self.input_field1 = tk.StringVar()

        self.create_frames_for_labels_and_entry_fields()
        self.menus()
        self.create_input_fields()
        self.position_input_fields()
        self.create_buttons()

    def create_frames_for_labels_and_entry_fields(self):
        self.frame1 = tk.Frame(self.window, relief=tk.RAISED, borderwidth=1)
        #self.frame2 = tk.Frame(self.window, relief=tk.RIDGE)
        self.frame2 = tk.Frame(self.window, relief=tk.RAISED, borderwidth=1)

        # the fill keyword argument to specify in which direction the frames should fill
        # the side keyword argument of .pack() specifies on which side of the window the widget should be placed.
        self.frame1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.frame2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def create_input_fields(self):
        # creating a label for input field 1
        self.field1_label = ttk.Label(self.frame1, width=15, text='Path for folder', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.frame1, textvariable=self.input_field1, font=('arial', 10, 'normal'))
        # default value for input field 1
        self.field1_entry.insert(tk.END, 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/04_udemy_Courses/__udemy_Learn_Python_With_20+_Real_World_Projects__/screenshots')

        # Placing the labels and entries in the required position using one of the 3 methods:
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

    def position_input_fields(self):
        self.field1_label.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)
        self.field1_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X, expand=tk.YES)

    def menus(self):
        # Menus
        menubar = tk.Menu(self.window)

        filemenu1 = tk.Menu(menubar, tearoff=0, background='blue', foreground='white')

        filemenu1.add_command(label="Select the folder", command=self.browse_for_folder1)

        menubar.add_cascade(label="Select the folder for screenshots", menu=filemenu1)

        self.window.config(menu=menubar)

    def create_buttons(self):
        # creating a button that will call the "method_for_button_COMPARE" method
        self.ok_button = ttk.Button(self.frame2, text='Take Screenshots', command=self.method_for_button_Take_Screenshots)

        # creating a button that will call the "quit" function
        self.quit_button = ttk.Button(self.frame2, text='Quit', command=self.window.destroy)

        self.ok_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)

    def method_for_button_Take_Screenshots(self):
        name1 = int(round(time.time()*1000))

        path = self.path1
        name2 = path + '\{}.png'.format(name1)
        time.sleep(5)
        img = pyautogui.screenshot(name2)
        print(f'Screenshot nr. {name1} is at path {path}')
        # img.show()

    def browse_for_folder1(self):
        self.path1 = filedialog.askdirectory()
        self.input_field1.set("")
        self.field1_entry.insert(tk.END, self.path1)
        print("Selected folder: ", self.path1)

        return self.path1


def main():
    # Create the entire GUI program
    my_GUI = CreateMenusFieldsButtons()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()


if __name__ == "__main__":
    main()
