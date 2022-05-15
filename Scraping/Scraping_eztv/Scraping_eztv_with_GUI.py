
# Program with input fields + buttons + message box  
  
import tkinter as tk
from tkinter import ttk
#from tkinter import filedialog
import tksheet

import requests
from bs4 import BeautifulSoup

import pandas as pd

#from HTML_code_for_eztv_site_for_Scraping2 import page_content

#import webbrowser



class Scraping_eztv():

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

        self.TV_Series = ''
        self.Title = []
        self.Magnet = []
        self.Zoink = []
        self.Size = []
        self.Released = []
        self.Seeds = []

        self.create_frame_for_labels_and_entry_fields()
        self.create_input_fields()
        self.position_input_fields()
        self.create_buttons()

    
    def create_frame_for_labels_and_entry_fields(self):
        #self.frame = tk.Frame(self.window, relief=tk.RIDGE)

        # the fill keyword argument to specify in which direction the frames should fill
        # the side keyword argument of .pack() specifies on which side of the window the widget should be placed.
        self.frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5) 

    def create_input_fields(self):
        # creating a label for input field 1
        self.field1_label = ttk.Label(self.frame, width=10, text = 'TV Series', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.frame, width=50, textvariable = self.input_field1, font=('arial', 10, 'normal')) 
        # default value for input field 1
        self.field1_entry.insert(tk.END, 'Your Honor')
       
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
        # creating a button that will call the "submit" function
        self.scraping_button=ttk.Button(self.frame, text = 'Scraping', command = self.scraping) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame, text = 'Quit', command = self.window.destroy)

        self.scraping_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)


    def create_a_sheet(self):
        self.sheet = tksheet.Sheet(self.window, width=1500, height=750)
        self.sheet.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        self.headers = ("Name","Torrent Magnet","Torrent Zoink","Size","Released", "Seeds")
        self.sheet.headers(self.headers)

        self.sheet.column_width(column=0, width=750, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=1, width=350, only_set_if_too_small=True, redraw=True)
        self.sheet.column_width(column=2, width=350, only_set_if_too_small=True, redraw=True)
        
        self.sheet.set_column_data(0, values=self.Title)
        self.sheet.set_column_data(1, values=self.Magnet)
        self.sheet.set_column_data(2, values=self.Zoink)
        self.sheet.set_column_data(3, values=self.Size)
        self.sheet.set_column_data(4, values=self.Released)
        self.sheet.set_column_data(5, values=self.Seeds)

        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu", "rc_select", "rc_insert_row", "rc_delete_row",
                       "copy", "cut", "paste", "delete", "undo", "edit_cell"))

        #self.sheet.extra_bindings([("cell_select", self.open_browser)])

        self.sheet.change_theme("light blue")


    def open_browser(self):
        """
        method to open the browser selecting a cell
        """
        print("cell_select")
            
        #webbrowser.open('http://google.com')


    # BINDING NEW RIGHT CLICK FUNCTION
    #self.sheet.bind("<Navigate to>", self.rc)



    def scraping(self):
        input1 = self.input_field1.get() # the string entered in the input field "TV Series"

        self.TV_Series = input1.replace(" ", "-")

        path = 'https://eztv.re/search/' + self.TV_Series

        page_content = requests.get(path).content
       
        soup = BeautifulSoup(page_content, 'html.parser')

        locator_line_hover_magnet = 'tr.forum_header_border td.forum_thread_post a.magnet'
        line_hover_magnet = soup.select('tr.forum_header_border td.forum_thread_post a.magnet')

        line_hover_zoink = soup.select('tr.forum_header_border td.forum_thread_post a.download_1')
        line_hover = soup.select('tr.forum_header_border td:nth-child(3)')

        line_hover_size = soup.select('tr.forum_header_border td:nth-child(4)')

        line_hover_released = soup.select('tr.forum_header_border td:nth-child(5)')

        line_hover_seeds = soup.select('tr.forum_header_border td:nth-child(6)')


        for item in line_hover_magnet:
            print(item.attrs['title'])

        for item in line_hover_magnet:
            self.Title.append(item.attrs['title'])
            self.Magnet.append(item.attrs['href'])


        #for item in line_hover:
        #    if ('class=download_1' in item.find_all('a')):
        #        self.Zoink.append(item.attrs['href'])
        #    else:
        #        self.Zoink.append(None)


        for item in line_hover_size:
            self.Size.append(item.string)

        for item in line_hover_released:
            self.Released.append(item.string)

        for item in line_hover_seeds:
            self.Seeds.append(item.string)
            

        # display the results in a sheet in window
        self.create_a_sheet()

        self.window.state('zoomed')
            
        print("Total torrents: ", len(line_hover_magnet))





def main():
    # Create the entire GUI program
    my_GUI = Scraping_eztv()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()

    df = pd.DataFrame({"Title" : my_GUI.Title, "Magnet" : my_GUI.Magnet, "Size": my_GUI.Size, "Released" : my_GUI.Released, "Seeds" : my_GUI.Seeds})

    # Converting to excel 
    df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/Scraping/eztv/eztv_torrents.xlsx', index = False)



if __name__ == "__main__":
    main()