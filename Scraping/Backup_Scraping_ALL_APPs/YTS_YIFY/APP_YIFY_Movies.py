
import requests

#import tkinter as tk
#from tkinter import ttk
#import tksheet

import pandas as pd
import numpy as np

import xlsxwriter
import io

import urllib.request

from pages.home_movies_page import HomeMoviesPage
from pages.details_movie_page import DetailsMoviePage

#from HTML_Home_YIFY import home_page_content # to avoid going to the site
#from HTML_Details_YIFY import details_page_content # to avoid going to the site

from parsers.home_movies_parser import HomeMoviesParser
from parsers.details_movie_parser import DetailsMovieParser

from GUI.create_fields_buttons import CreateFieldsButtons
from GUI.create_a_sheet import CreateSheet

from format_Excel.format_cells import FormatCells


class Scraping_YIFY:

    def __init__(self):
        pass

        #self.Name = []
        #self.Year = []
        #self.Genre = []
        #self.Torrent = []
        #self.IMDB = []


    #def scraping_when_button_clicked(self):

        ##path = 'https://yts.mx/'
        ##page_content = requests.get(path).content

        #home_page = HomeMoviesPage(home_page_content)
        #popular_movies = home_page.popular_movies

        ##latest_movies = home_page.latest_movies
        ##upcoming_movies = home_page.upcoming_movies

        #print("POPULAR Movies: ", popular_movies)
        #for movie in popular_movies:
        #    print(movie)
        #    details_page_path = movie.details_page_path # the path for the page with details is obtained
        #    details_page_content = requests.get(details_page_path).content
        #    details_of_a_movie = DetailsMoviePage(details_page_content)

        #    scrap.Name.append(details_of_a_movie.name)
        #    scrap.Year.append(details_of_a_movie.year)
        #    scrap.Genre.append(details_of_a_movie.genre)
        #    scrap.Torrent.append(details_of_a_movie.torrent)
        #    scrap.IMDB.append(details_of_a_movie.imdb_link)

        #    print("Details: ", details_of_a_movie)


        ##print(latest_movies)
        ##print(upcoming_movies)


def main():

    # Create the entire GUI program
    my_GUI = CreateFieldsButtons()
   
    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()

    # Create a Data Frame using pandas

    df = pd.DataFrame({"Movie" : my_GUI.Name, "Year" : my_GUI.Year, "Genre" : my_GUI.Genre, "Quality" : my_GUI.Quality, "IMDB Rating" : my_GUI.Imdb_Rating, "IMDB Votes" : my_GUI.Imdb_Votes, "Torrent" : my_GUI.Torrent, "IMDB" : my_GUI.Imdb, 'Img' : my_GUI.Image})


    #a = {"Movie" : my_GUI.Name, "Year" : my_GUI.Year, "Genre" : my_GUI.Genre, "Quality" : my_GUI.Quality, "IMDB Rating" : my_GUI.Imdb_Rating, "IMDB Votes" : my_GUI.Imdb_Votes,"Torrent" : my_GUI.Torrent, "IMDB" : my_GUI.Imdb, 'Img' : my_GUI.Image}
    #df = pd.DataFrame.from_dict(a, orient='columns')
    #df.transpose()

    # Set the index to start from 1
    df.index = np.arange(1, len(df)+1)

    # Converting to excel 
    df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/Scraping/YTS_YIFY/YIFY_torrents.xlsx', index = True, header=True, sheet_name = 'Popular Movies')

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/Scraping/YTS_YIFY/YIFY_torrents.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Popular Movies')

    # Get the xlsxwriter objects from the dataframe writer object.
    workbook  = writer.book
    worksheet = writer.sheets['Popular Movies']

    # Widen the first 7 columns to make the text clearer.
    worksheet.set_column(1, 1, 30) #Movie
    worksheet.set_column(2, 2, 10) #Year
    worksheet.set_column(3, 3, 25) #Genre
    worksheet.set_column(4, 4, 15) #Quality
    worksheet.set_column(5, 5, 5) #IMDB Rating
    worksheet.set_column(6, 6, 5) #IMDB Nr. of Votes
    worksheet.set_column(7, 7, 75) #Torrent
    worksheet.set_column(8, 8, 40) #Imdb
    worksheet.set_column(9, 9, 20) #Img

    # Insert an image: https://xlsxwriter.readthedocs.io/worksheet.html#worksheet-set-column
    #url = 'https://yts.mx/assets/images/movies/outside_the_wire_2021/medium-cover.jpg'
    #image_data = io.BytesIO(urllib.request.urlopen(url).read())
    #worksheet.insert_image('H2', 'c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/Scraping/YTS_YIFY/img.jpg', {'x_scale': 0.5, 'y_scale': 0.5})
    #worksheet.insert_image('H2', url, {'image_data': image_data})

    workbook.close()


if __name__ == "__main__":
    main()



