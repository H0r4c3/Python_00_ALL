'''

'''


class AppScraper:
    pass



def main():
    from GUI_for_scraping import GUIForScraping

    # Create the entire GUI
    my_GUI = GUIForScraping()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()


    #df = pd.DataFrame({"Field 1" : my_GUI.input1_list, "Field 2" : my_GUI.input2_list, "Field 3" : my_GUI.input3_list}, index=[0])

    # Converting to excel 
    #df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/GUI/Templates_Classes/Output_Excel.xlsx', index = False)



if __name__ == "__main__":
    main()
