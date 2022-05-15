
import pandas as pd
from bs4 import BeautifulSoup

import requests

from HTML_6Martie import page_content_6Martie
from HTML_7Martie import page_content_7Martie
from HTML_Luna_Martie import page_content_Luna_Martie
from HTML_Luna_Martie_Moldova_Noua import page_content_luna_martie_Moldova_Noua
from HTML_DayDetails_Moldova_Noua import page_content_day_details_Moldova_Noua


from month_page import MonthPage
from day_page import DayPage
from day_page_parser import DayPageParser

from locators.MONTH_Locators import MonthLocators

#file1_path = 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/ROVACCINARE/HTML_6Martie.py'
#file2_path = 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/ROVACCINARE/HTML_7Martie.py'
#file3_path = 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/ROVACCINARE/HTML_Luna_Martie.py'


class Scraping_ROVACCINARE:
    def __init__(self, content_page):
        #self.soup_Month_Martie = BeautifulSoup(page_content_Luna_Martie, 'html.parser')
        self.content_page = content_page

        self.Data = []
        self.Ore = []
        self.Locuri = []
        self.Butoane = []
 

    def details_for_every_row(self):
        day_page_object = DayPage(self.content_page) # create an instance of "DayPage" class having argument content_page = page_content_day_details_Moldova_Noua

        rows_with_ore_in_day_page = day_page_object.rows_with_ore_in_day_page # list with all the rows with "ore"
        rows_with_locuri_in_day_page = day_page_object.rows_with_locuri_in_day_page # list with all the rows with "locuri"
        data_in_day_page = day_page_object.data_in_day_page

        for row in rows_with_ore_in_day_page:
            self.Data.append(data_in_day_page)
            self.Ore.append(row.ora)

        for row in rows_with_locuri_in_day_page:
            self.Locuri.append(row.locuri_disponibile)
            self.Butoane.append(row.butonul_selecteaza)   
                

def main():
    #path = 'https://programare.vaccinare-covid.gov.ro/#/planning/recipient/3179238'
    #path = 'https://programare.vaccinare-covid.gov.ro/scheduling/api/time_slots/month_available_places'

    #response = requests.get("https://programare.vaccinare-covid.gov.ro/scheduling/api/time_slots/month_available_places")
    #print("Response: ", response)

    #page_content_Luna_Martie = requests.get(path).content

    
    #print("Cells in Month Page: ", cells_in_month_page)

    month_page_object = MonthPage(page_content_luna_martie_Moldova_Noua) # create an instance of "MonthPage" class having argument content_page = page_content_Luna_Martie
    cells_in_month_page = month_page_object.cells_in_month_page # the list with all the cells/days in a month (the attribute "cells_in_month_page" applied on the object "month_page")


    day_page_object = DayPage(page_content_day_details_Moldova_Noua) # create an instance of "DayPage" class having argument content_page = page_content_6Martie

    data_in_day_page = day_page_object.data_in_day_page
    rows_with_ore_in_day_page = day_page_object.rows_with_ore_in_day_page
    rows_with_locuri_in_day_page = day_page_object.rows_with_locuri_in_day_page
    
    
    vaccin = Scraping_ROVACCINARE(page_content_day_details_Moldova_Noua)
    vaccin.details_for_every_row()
    vaccin.Locuri.append("Lipseste")
    vaccin.Butoane.append("Lipseste")
    #print("Data: ", vaccin.Data)
    #print("Ore: ", vaccin.Ore)
    #print("Locuri: ", vaccin.Locuri)
    #print("Butoane: ", vaccin.Butoane)

    # Create a dictionary with the details from details page
    Dict_details_page = {"Data" : vaccin.Data, "Ora" : vaccin.Ore, "Locuri" : vaccin.Locuri, "Butoane" : vaccin.Butoane} 
    df = pd.DataFrame(Dict_details_page)

    print(df)

    # Converting to excel 
    df.to_excel('C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/ROVACCINARE/ROVACCINARE.xlsx', index = True, sheet_name = 'Data')


    
        

if __name__ == "__main__":
    main()
