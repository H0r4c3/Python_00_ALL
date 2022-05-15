import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import os
from pathlib import Path


class All_User_Input_Widgets():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Horace")

        #self.create_widgets()

        self.input1 = tk.StringVar()
        #self.folder_path = tk.StringVar()

        self.data_entry_frame()
        self.menus()
        self.buttons()
        self.choosing_from_lists_frame()

        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        self.path = ''
        self.extension = ''

        self.all_dirs = []
        self.all_subtitle_files = []


    def browse_for_folder(self):
        self.path = filedialog.askdirectory()
        
        self.input1.set(self.path)

        print("Selected path: ", self.path)

        return self.path

    '''
    def fill_folder_path_field(self):
        text1 = self.input1.get()
        print(text1)
        return text1
    '''


    # Get the list of all files in directory tree at given path
    def get_all_files(self, dir_path, extension):
        extension = self.my_listbox.get(tk.ACTIVE)
        for dirpath, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(extension):

                    #self.convert_line_endings(file)

                    self.all_subtitle_files.append(file)
                    [self.all_dirs.append(dir) for dir in dirs if dir not in self.all_dirs]
        print("All directories: ", self.all_dirs)
        #self.my_text.insert(tk.END, self.all_dirs)
        print("All files: ")
        for item in self.all_subtitle_files:
            print(item)
        #self.my_text.insert(tk.END, self.all_subtitle_files)
        self.all_dirs = []
        self.all_subtitle_files = []
        return self.all_dirs, self.all_subtitle_files


    def commands_frame(self):
        
        # The Commands frame
        # cmd_frame = ttk.LabelFrame(self.window, text="Commands", padx=5, pady=5, relief=tk.RIDGE)
        cmd_frame = ttk.LabelFrame(self.window, text="Commands", relief=tk.RIDGE)
        cmd_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        button_label = ttk.Label(cmd_frame, text="tk.Button")
        button_label.grid(row=1, column=1, sticky=tk.W, pady=3)

        button_label = ttk.Label(cmd_frame, text="ttk.Button")
        button_label.grid(row=2, column=1, sticky=tk.W, pady=3)

        menu_label = ttk.Label(cmd_frame, text="Menu (see examples above)")
        menu_label.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=3)

        my_button = tk.Button(cmd_frame, text="do something")
        my_button.grid(row=1, column=2)

        my_button = ttk.Button(cmd_frame, text="do something")
        my_button.grid(row=2, column=2)

    def data_entry_frame(self):

        # The Data entry frame
        entry_frame = ttk.LabelFrame(self.window, text="", relief=tk.RIDGE)
        entry_frame.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

        entry_label = ttk.Label(entry_frame, text="Entry")
        entry_label.grid(row=1, column=1, sticky=tk.W + tk.N)

        text_label = ttk.Label(entry_frame, text="Text")
        text_label.grid(row=2, column=1, sticky=tk.W + tk.N)

        #scale_label = ttk.Label(entry_frame, text="tk.Scale")
        #scale_label.grid(row=4, column=1, sticky=tk.W)

        #scale_label2 = ttk.Label(entry_frame, text="ttk.Scale")
        #scale_label2.grid(row=5, column=1, sticky=tk.W)

        my_entry = ttk.Entry(entry_frame, textvariable = self.input1, width=40)
        my_entry.grid(row=1, column=2, sticky=tk.W, pady=3)

        my_text = tk.Text(entry_frame, height=5, width=30)
        my_text.grid(row=2, column=2)
        #my_text.insert(tk.END, "An example of multi-line\ninput")

        '''
        my_spinbox = tk.Spinbox(entry_frame, from_=0, to=10, width=5, justify=tk.RIGHT)
        my_spinbox.grid(row=3, column=2, sticky=tk.W, pady=3)

        my_scale = tk.Scale(entry_frame, from_=0, to=100, orient=tk.HORIZONTAL, width=8, length=200)
        my_scale.grid(row=4, column=2, sticky=tk.W)

        my_scale = ttk.Scale(entry_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200)

        my_scale.grid(row=5, column=2, sticky=tk.W)
        '''

    def choices_frame(self):

        # The Choices frame
        switch_frame = ttk.LabelFrame(self.window, text="Choices", relief=tk.RIDGE, padding=6)
        switch_frame.grid(row=2, column=2, padx=6, sticky=tk.E + tk.W + tk.N + tk.S)

        checkbox_label = ttk.Label(switch_frame, text="ttk.Checkbutton")
        checkbox_label.grid(row=1, rowspan=3, column=1, sticky=tk.W + tk.N)

        entry_label = ttk.Label(switch_frame, text="ttk.Radiobutton")
        entry_label.grid(row=4, rowspan=3, column=1, sticky=tk.W + tk.N)

        checkbutton1 = ttk.Checkbutton(switch_frame, text="On-off switch 1")
        checkbutton1.grid(row=1, column=2)
        checkbutton2 = ttk.Checkbutton(switch_frame, text="On-off switch 2")
        checkbutton2.grid(row=2, column=2)
        checkbutton3 = ttk.Checkbutton(switch_frame, text="On-off switch 3")
        checkbutton3.grid(row=3, column=2)

        self.radio_variable = tk.StringVar()
        self.radio_variable.set("0")

        radiobutton1 = ttk.Radiobutton(switch_frame, text="Choice One of three",
                                       variable=self.radio_variable, value="0")
        radiobutton2 = ttk.Radiobutton(switch_frame, text="Choice Two of three",
                                       variable=self.radio_variable, value="1")
        radiobutton3 = ttk.Radiobutton(switch_frame, text="Choice Three of three",
                                       variable=self.radio_variable, value="2")
        radiobutton1.grid(row=4, column=2, sticky=tk.W)
        radiobutton2.grid(row=5, column=2, sticky=tk.W)
        radiobutton3.grid(row=6, column=2, sticky=tk.W)

    def choosing_from_lists_frame(self):
        # The Choosing from lists frame
        fromlist_frame = ttk.LabelFrame(self.window, relief=tk.RIDGE)
        fromlist_frame.grid(row=0, column=2, sticky=tk.E + tk.W + tk.N + tk.S, padx=6)

        listbox_label = tk.Label(fromlist_frame, text="Select the extension of files")
        listbox_label.grid(row=0, column=1, sticky=tk.W + tk.N)

        #combobox_label = tk.Label(fromlist_frame, text="ttk.Combobox")
        #combobox_label.grid(row=2, column=1, sticky=tk.W + tk.N)

        self.my_listbox = tk.Listbox(fromlist_frame, height=3)

        for item in ["srt", "sub", "txt"]:
            self.my_listbox.insert(tk.END, item)

        self.my_listbox.grid(row=1, column=1)

        self.extension = self.my_listbox.get(tk.ACTIVE)

       
        #self.combobox_value = tk.StringVar()
        #my_combobox = ttk.Combobox(fromlist_frame, height=4, textvariable=self.combobox_value)
        #my_combobox.grid(row=2, column=2)
        #my_combobox['values'] = ("Choice one", "Choice two", "Choice three", "Choice four")
        #my_combobox.current(0)

        return self.extension
       

    def menus(self):

        # Menus
        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff=0)
        #filemenu.add_command(label="Select", command=filedialog.askdirectory)
        filemenu.add_command(label="Select", command=self.browse_for_folder)
        #filemenu.add_command(label="Save", command=filedialog.asksaveasfilename)
        #filemenu.add_separator()
        #filemenu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="Folder", menu=filemenu)

        self.window.config(menu=menubar)


    #def select_extension(self):

        #all_items_in_my_listbox = self.my_listbox.get(0, tk.END) # tuple with text of all items in Listbox
        #self.extension = self.my_listbox.get(tk.ACTIVE)

        #return self.extension


    def buttons(self):

        # OK button in the lower right corner
        ok_button = ttk.Button(self.window, text="OK", command=lambda: self.get_all_files(self.path, self.extension))
        ok_button.grid(row=4, column=1)

        # Quit button in the lower right corner
        quit_button = ttk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=4, column=3)


    def convert_line_endings(self, file_path):

        # replacement strings
        UNIX_LINE_ENDING = b'\n'
        WINDOWS_LINE_ENDING = b'\r\n'
    
        # file path
        #file_path = r"c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Convert_all_line_endings_in_a_file/Subtitle_NOK.srt"
    
        # Open subtitle file and read the content
        with open(file_path, 'rb') as open_file:
            content = open_file.read()
    
        content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)
    
        with open(file_path, 'wb') as open_file:
            open_file.write(content)


def main():
    # Create the entire GUI program
    my_GUI = All_User_Input_Widgets()
    
    # Start the GUI event loop
    my_GUI.window.mainloop()

if __name__ == "__main__":
    main()
