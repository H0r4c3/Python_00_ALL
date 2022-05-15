# Program with input fields + buttons + message box  
  
import tkinter as tk
from tkinter import ttk
import tksheet
import pandas as pd
import requests

from pages.home_movies_page import HomeMoviesPage
from pages.browse_movies_page import BrowseMoviesPage
from pages.details_movie_page import DetailsMoviePage
from pages.imdb_page import ImdbPage

#from HTML_Home_YIFY import home_page_content # to avoid going to the site
#from HTML_Browse_YIFY import browse_page_content # to avoid going to the site
#from HTML_Details_YIFY import details_page_content # to avoid going to the site

from parsers.home_movies_parser import HomeMoviesParser
from parsers.details_movie_parser import DetailsMovieParser

from GUI.create_a_sheet import CreateSheet

class CreateFieldsButtons:

    def __init__(self):
        self.Name = []
        self.Year = []
        self.Genre = []
        self.Quality = []
        self.Torrent = []
        self.Imdb = []
        self.Image = []
        self.Imdb_Rating = []
        self.Imdb_Votes = []


        self.window = tk.Tk()
        self.window.title("YIFY")
        self.frame = tk.Frame(self.window, relief=tk.RIDGE)

        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        ## declaring string variable for storing the input strings
        self.input_field1 = tk.StringVar() 
        #self.input_field2 = tk.StringVar() 
        #self.input_field3 = tk.StringVar()

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
        self.field1_entry.insert(tk.END, 'Click on Scraping button')
       
        ## creating a label for input field 2
        #self.field2_label = ttk.Label(self.frame, width=10, text = 'Input Field 2', font = ('arial', 10, 'bold')) 
        ## creating an entry for input field 2
        #self.field2_entry=ttk.Entry(self.frame, width=50, textvariable = self.input_field2, font = ('arial', 10,'normal'))
    
        ## creating a label for input field 3
        #self.field3_label = ttk.Label(self.frame, width=10, text = 'Input Field 3', font = ('arial', 10, 'bold')) 
        ## creating an entry for input field 3
        #self.field3_entry=ttk.Entry(self.frame, width=50, textvariable = self.input_field3, font = ('arial', 10,'normal'))

        # Placing the labels and entries in the required position using one of the 3 methods: 
        '"place" = You specify the exact size and position of each widget.'
        '"pack" = You specify the size and position of each widget relative to each other.'
        '"grid" = You place widgets in a cell of a 2-dimensional table defined by rows and columns.'

    def position_input_fields(self):
        self.field1_label.pack(padx=5, pady=5, side=tk.LEFT)
        self.field1_entry.pack(padx=1, pady=5, side=tk.LEFT)


    def create_buttons(self):
        from APP_YIFY_Movies import Scraping_YIFY

        # creating a button that will call the "method_for_button_OK" method
        self.ok_button=ttk.Button(self.frame, text = 'Scraping', command = self.scraping_when_button_clicked2) 
    
        # creating a button that will call the "quit" function  
        self.quit_button=ttk.Button(self.frame, text = 'Quit', command = self.window.destroy)

        self.ok_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)

     
        #""" Defining a function that will get the input text 1, input text 2, input text 3 and print them on the screen """
        #self.input1 = self.input_field1.get() # the string entered in the input field 1
        #self.input2 = self.input_field2.get() # the string entered in the input field 2
        #self.input3 = self.input_field3.get() # the string entered in the input field 3
      
        #print("Input text 1 : " + self.input1) 
        #print("Input text 2 : " + self.input2) 
        #print("Input text 3 : " + self.input3)
      
        #self.input_field1.set("") 
        #self.input_field2.set("") 
        #self.input_field3.set("")

        #self.input1_list = self.input1.split(',')
        #self.input2_list = self.input2.split(',')
        #self.input3_list = self.input3.split(',')

    def details_for_every_movie(self, movies_group):
        for movie in movies_group:
            # details for each movie in the list with all movies
            details_page_path = movie.details_page_path # the path for the page with details is obtained
            details_page_content = requests.get(details_page_path).content # get the details page content for every movie
            details_of_a_movie = DetailsMoviePage(details_page_content) # get the details (from the Details Page) for every movie

            self.Name.append(details_of_a_movie.name_from_details_page)
            self.Year.append(movie.year_home)
            self.Genre.append(details_of_a_movie.genre_from_details_page)
            self.Quality.append(details_of_a_movie.quality_from_details_page)
            self.Torrent.append(details_of_a_movie.torrent_from_details_page)
            self.Imdb.append(details_of_a_movie.imdb_link_from_details_page)
            self.Image.append(movie.image_home)

            if details_of_a_movie.imdb_link_from_details_page != None:
                imdb_page_path = details_of_a_movie.imdb_link_from_details_page # the path for the Imdb page is obtained
                imdb_page_path = imdb_page_path + 'reference'
                print('imdb_page_path: ', imdb_page_path)
                imdb_page_content = requests.get(imdb_page_path).content # get the Imdb page content for every movie
                imdb_details_of_a_movie = ImdbPage(imdb_page_content) # get the details (from the Imdb Page) for every movie
                self.Imdb_Rating.append(imdb_details_of_a_movie.rating_from_imdb_page)
                print("rating_from_imdb_page: ", imdb_details_of_a_movie.rating_from_imdb_page)
                self.Imdb_Votes.append(imdb_details_of_a_movie.nr_of_votes_from_imdb_page)
                print("nr_of_votes_from_imdb_page: ", imdb_details_of_a_movie.nr_of_votes_from_imdb_page)
            else: 
                print("No imdb link in details page")

            #print("Home Page: ", movie)
           
            #print("Details Page: ", details_of_a_movie)

            #print("IMDB Page: ", imdb_details_of_a_movie)


    def scraping_when_button_clicked(self):
        path_home = 'https://yts.mx/'
        path_browse = 'https://yts.mx/browse-movies'
        path_browse_page2 = 'https://yts.mx/browse-movies?page=2'

        #home_page_content = requests.get(path_home).content
        browse_page_content = requests.get(path_browse).content

        #home_page = HomeMoviesPage(home_page_content) # create an instance of "HomeMoviesPage" class having argument page = home_page_content
        

        #popular_movies = home_page.popular_movies # the list with all the 4 popular movies (the attribute "popular_movies" applied on the object "home_page")
        #print("\nPOPULAR Movies: ", popular_movies)

        #self.details_for_every_movie(popular_movies) # apply the method "details_for_every_movie" on the list with the 4 popular movies

        #latest_movies = home_page.latest_movies
        #print("\nLATEST movies: ", latest_movies)

        #self.details_for_every_movie(latest_movies)

        #upcoming_movies = home_page.upcoming_movies
        #print("UPCOMING movies: ", upcoming_movies)

        #self.details_for_every_movie(upcoming_movies)


        browse_page = BrowseMoviesPage(browse_page_content) # create an instance of "BrowseMoviesPage" class having argument page = browse_page_content

        browse_movies_list = browse_page.browse_movies # the list with all movies in the browse page (the attribute "browse_movies" applied on the object "browse_page")
        print("\nBROWSE Movies: ", browse_movies_list)

        self.details_for_every_movie(browse_movies_list) # apply the method "details_for_every_movie" on the list with all the movies in Browse page

        #display the results in a sheet in window
        self.sheet_object = CreateSheet(self)
        self.sheet = self.sheet_object.create_a_sheet()

        self.window.state('zoomed')


    def scraping_when_button_clicked2(self):
        #path_browse = 'https://yts.mx/browse-movies'
        #path_browse_page2 = 'https://yts.mx/browse-movies?page=2'
        for i in range (1, 5):
            path_browse = 'https://yts.mx/browse-movies?page=' + str(i)
            print(path_browse)
            browse_page_content = requests.get(path_browse).content

            browse_page = BrowseMoviesPage(browse_page_content) # create an instance of "BrowseMoviesPage" class having argument page = browse_page_content

            browse_movies = browse_page.browse_movies # the list with all movies in the browse page (the attribute "browse_movies" applied on the object "browse_page")
            print("\nBROWSE Movies: ", browse_movies)

            self.details_for_every_movie(browse_movies) # apply the method "details_for_every_movie" on the list with all the movies in Browse page

        #display the results in a sheet in window
        self.sheet_object = CreateSheet(self)
        self.sheet = self.sheet_object.create_a_sheet()

        self.window.state('zoomed')