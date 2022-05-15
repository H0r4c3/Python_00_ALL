# Program with input fields + buttons + message box  
  
import tkinter as tk
from tkinter import ttk
#from tkinter import filedialog
import tksheet
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


class GUIForScraping():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GUI for Scraping")
        self.frame = tk.Frame(self.window, relief=tk.RIDGE)

        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # declaring string variable for storing the input strings
        self.input_field1 = tk.StringVar() 
        self.input_field2 = tk.StringVar() 
        self.input_field3 = tk.StringVar()

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

        default_url = 'https://www.emag.ro/search/telefoane-mobile/m62/c?ref=list'
        default_element_cards = "class"
        default_attrs = "card-item card-standard js-product-data"
        default_element1 = "data-zone"
        default_attrs1 = "title"


        # creating a label for input field 1
        self.field1_label = ttk.Label(self.frame1, width=20, text = 'URL for scraping:', font=('arial', 10, 'bold'))
        # creating an entry for input field 1
        self.field1_entry = ttk.Entry(self.frame1, width=100, textvariable = self.input_field1, font=('arial', 10, 'normal')) 
        # default value for input field 1
        self.field1_entry.insert(tk.END, default_url)
        
        
        # creating a label for input field 2
        self.field2a_label = ttk.Label(self.frame2, width=20, text = 'Cards:', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 2
        self.field2a_entry=ttk.Entry(self.frame2, width=10, textvariable = self.input_field2, font = ('arial', 10,'normal'))
        # default value for input field 2
        self.field2a_entry.insert(tk.END, default_element_cards)
        
        self.field2b_label = ttk.Label(self.frame2, width=20, text = 'Attrs:', font = ('arial', 10, 'bold'))
        self.field2b_entry=ttk.Entry(self.frame2, width=100, textvariable = self.input_field2, font = ('arial', 10,'normal'))
        self.field2b_entry.insert(tk.END, default_attrs)
        
    
        # creating a label for input field 3
        self.field3a_label = ttk.Label(self.frame3, width=20, text = 'Element1:', font = ('arial', 10, 'bold')) 
        # creating an entry for input field 3
        self.field3a_entry=ttk.Entry(self.frame3, width=10, textvariable = self.input_field3, font = ('arial', 10,'normal'))
        # default value for input field 3
        self.field3a_entry.insert(tk.END, default_element1)
        
        self.field3b_label = ttk.Label(self.frame3, width=20, text = 'Attrs1:', font = ('arial', 10, 'bold'))
        self.field3b_entry=ttk.Entry(self.frame3, width=100, textvariable = self.input_field2, font = ('arial', 10,'normal'))
        self.field3b_entry.insert(tk.END, default_attrs1)

        # Placing the labels and entries in the required position using one of the 3 methods: 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

    def position_input_fields(self):
        self.field1_label.pack(padx=5, pady=5, side=tk.LEFT)
        self.field1_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)
        
        
        self.field2a_label.pack(padx=5, pady=5, side=tk.LEFT)        
        self.field2a_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)
        
        self.field2b_label.pack(padx=5, pady=5, side=tk.LEFT)        
        self.field2b_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)


        self.field3a_label.pack(padx=5, pady=5, side=tk.LEFT)
        self.field3a_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)
        
        self.field3b_label.pack(padx=5, pady=5, side=tk.LEFT)
        self.field3b_entry.pack(padx=1, pady=5, side=tk.LEFT, fill=tk.X)

    def create_buttons(self):
        # creating a button that will call the "method_for_button_OK" method
        self.scrap_button=ttk.Button(self.frame4, text = 'Scrap', command = self.scraping_when_button_clicked) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame4, text = 'Quit', command = self.window.destroy)

        # position the buttons
        self.scrap_button.pack(padx=5, pady=5, side=tk.LEFT)
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

    def create_text_widget(self):
        #self.text.delete(1.0,END)
        self.text = tk.Text(self.frame5, height=45, width=200)
        #self.scroll = tk.Scrollbar(self.frame5, command=text.yview)
        #self.text.configure(yscrollcommand=scroll.set)
        #self.text.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        #self.text.tag_configure('big', font=('Verdana', 20, 'bold'))
        self.text.tag_configure('color1', foreground='blue', font=('Arial', 12, 'bold'))
        self.text.tag_configure('color2', foreground='red', font=('Arial', 12, 'bold'))
        #self.text.insert(tk.END, text, 'color')
        self.text.pack(side=tk.LEFT)
        #self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def fill_text_widget(self, scraped_text):
        self.text.delete('1.0', 'end')
        self.text.insert(tk.END, scraped_text, 'color1')

    def scraping_when_button_clicked(self):
        
        # clear the text widget
        self.text.delete('1.0', 'end')
        

        url = self.input_field1.get() # the string entered in the input field 1
        input2 = json.loads(self.input_field2.get()) # the string entered in the input field 2
        input3 = json.loads(self.input_field3.get()) # the string entered in the input field 3

        input4 = {"class" : "product-new-price"}
        
        
        # url = 'https://www.emag.ro/search/telefoane-mobile/m62/c?ref=list'
        # input2 = {"class" : "card-item card-standard js-product-data"}
        # input3 = {"data-zone" : "title"}
        # input4 = {"class" : "product-new-price"}
        
        response = requests.get(url) # -> 200, if the page is found
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # scraping
        cards = soup.find_all("div", attrs=input2)

        for card in cards:
            title = card.find("a", attrs=input3)
            price = card.find("p", attrs=input4)
            #colors = card.find("a", attrs={"class" : "btn btn-xs btn-alt gtm_139rp27 js-product-url"})
            
            print(f'Title: {title.text}, Price: {price.text[:-6] + price.text[-4:]}')
            
            scraped_title = f'Title: {title.text}   '
            self.text.insert(tk.END, scraped_title, 'color1')
            scraped_price = f'Price: {price.text[:-6] + price.text[-4:]}\n'
            self.text.insert(tk.END, scraped_price, 'color2')
        
        
        
        # # scraping
        # cards = soup.find_all("div", attrs={"class" : "card-item card-standard js-product-data"})
        # print(cards)

        # for card in cards:
        #     title = card.find("a", attrs={"data-zone" : "title"})
        #     price = card.find("p", attrs={"class" : "product-new-price"})
        #     #colors = card.find("a", attrs={"class" : "btn btn-xs btn-alt gtm_139rp27 js-product-url"})
        
            #print(f'Title: {title.text}, Price: {price.text[:-6] + price.text[-4:]}, Colors: {colors.text}')
            # print(f'Title: {title.text}, Price: {price.text[:-6] + price.text[-4:]}')
            
            # scraped_title = f'Title: {title.text}   '
            # self.text.insert(tk.END, scraped_title, 'color1')
            # scraped_price = f'Price: {price.text[:-6] + price.text[-4:]}\n'
            # self.text.insert(tk.END, scraped_price, 'color2')
        
        
        # display the results in a sheet in window
        #self.sheet_object = CreateSheet(self)
        #self.sheet = self.sheet_object.create_a_sheet(self.input1_list, self.input2_list, self.input3_list)

        #self.window.state('zoomed')


def main():
    # Create the entire GUI
    my_GUI = GUIForScraping()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()

if __name__ == "__main__":
    main()