# Program with input fields + buttons + message box  
  
import tkinter as tk
from tkinter import ttk
#from tkinter import filedialog
import tksheet
import requests
from bs4 import BeautifulSoup
import pandas as pd

from all_paragraphs_for_parsing import AllParagraphsForParsing

#from create_a_sheet import CreateSheet

class CreateFieldsButtons():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Testing Locators")
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

        self.create_frames_for_labels_and_entry_fields_and_buttons()
        self.create_input_fields()
        self.position_input_fields()
        self.create_buttons()
        self.create_text_widget()

    
    def create_frames_for_labels_and_entry_fields_and_buttons(self):
        self.frame1 = tk.Frame(self.window, relief=tk.RIDGE)
        self.frame2 = tk.Frame(self.window, relief=tk.RIDGE)
        self.frame3 = tk.Frame(self.window, relief=tk.RIDGE)
        self.frame4 = tk.Frame(self.window, relief=tk.RIDGE)
        self.frame5 = tk.Frame(self.window, relief=tk.RIDGE)

        # the fill keyword argument to specify in which direction the frames should fill
        # the side keyword argument of .pack() specifies on which side of the window the widget should be placed.
        self.frame1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5) 
        self.frame2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.frame3.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.frame4.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.frame5.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def create_input_fields(self):
        default_path = 'https://books.toscrape.com/'
        default_locator_paragraphs = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
        default_locator_details = 'article.product_pod h3 a[title]'

        #default_path = 'https://www.readytowear.ro/barbati/imbracaminte/geci/geci-de-piele-barbati/geaca-de-piele-naturala-barbati-gipsy-bleumarin-alb-murdar/'
        #default_locator_paragraphs = '#content > div.product-info > div.right > div.price'
        #default_locator_details = 'span.txt_price'
        #default_locator_paragraphs = '#content > div.product-info'
        #default_locator_details = 'div.right'

        # creating a label for input field 1
        self.field1_label = ttk.Label(self.frame1, width=23, text = 'Path for scraping:', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.frame1, width=100, textvariable = self.input_field1, font=('arial', 10, 'normal')) 
        # default value for input field 1
        self.field1_entry.insert(tk.END, default_path)
       
        # creating a label for input field 2
        self.field2_label = ttk.Label(self.frame2, width=23, text = 'Location for paragraphs:', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 2
        self.field2_entry=ttk.Entry(self.frame2, width=100, textvariable = self.input_field2, font = ('arial', 10,'normal'))
        # default value for input field 2
        self.field2_entry.insert(tk.END, default_locator_paragraphs)
    
        # creating a label for input field 3
        self.field3_label = ttk.Label(self.frame3, width=23, text = 'Location for a detail:', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 3
        self.field3_entry=ttk.Entry(self.frame3, width=100, textvariable = self.input_field3, font = ('arial', 10,'normal'))
        # default value for input field 3
        self.field3_entry.insert(tk.END, default_locator_details)

        # Placing the labels and entries in the required position using one of the 3 methods: 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

    def position_input_fields(self):
        self.field1_label.pack(padx=5, pady=5, side=tk.LEFT)
        self.field1_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)

        self.field2_label.pack(padx=5, pady=5, side=tk.LEFT)        
        self.field2_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)

        self.field3_label.pack(padx=5, pady=5, side=tk.LEFT)
        self.field3_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)

    def create_buttons(self):
        # creating a button that will call the "method_for_button_OK" method
        self.ok_button=ttk.Button(self.frame4, text = 'OK', command = self.scraping_when_button_clicked) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame4, text = 'Quit', command = self.window.destroy)

        # position the buttons
        self.ok_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)

    def create_text_widget(self):
        #self.text.delete(1.0,END)
        self.text = tk.Text(self.frame5, height=45, width=200)
        #self.scroll = tk.Scrollbar(self.frame5, command=text.yview)
        #self.text.configure(yscrollcommand=scroll.set)
        #self.text.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        #self.text.tag_configure('big', font=('Verdana', 20, 'bold'))
        self.text.tag_configure('color', foreground='#476042', font=('Arial', 12, 'bold'))
        #self.text.insert(tk.END, text, 'color')
        self.text.pack(side=tk.LEFT)
        #self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def fill_text_widget(self, text):
        self.text.delete('1.0', 'end')
        self.text.insert(tk.END, text, 'color')

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

    def scraping_when_button_clicked(self):
        #path = 'https://www.readytowear.ro/barbati/imbracaminte/geci/geci-de-piele-barbati/geaca-de-piele-naturala-barbati-gipsy-bleumarin-alb-murdar'
        #path = 'https://books.toscrape.com/'
        allparagraphsparsed = []
        messages_string = ''

        path = self.input_field1.get()

        page_content = requests.get(path).content

        PARAGRAPHS_locator = self.input_field2.get()
        DETAIL_locator = self.input_field3.get()

        paragraphs_object = AllParagraphsForParsing(page_content, PARAGRAPHS_locator, DETAIL_locator)
        
        allparagraphsparsed = paragraphs_object.allparagraphs # a list of strings (details)

        for item in (allparagraphsparsed):
            messages_string = messages_string + str(item) + '\n'
            print(item)

        self.fill_text_widget(messages_string)


        #msg = messagebox.showinfo("Text", messages_string)

        # display the results in a sheet in window
        #self.sheet_object = CreateSheet(self)
        #self.sheet = self.sheet_object.create_a_sheet(self.input1_list, self.input2_list, self.input3_list)

        #self.window.state('zoomed')

