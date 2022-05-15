'''
https://www.readytowear.ro/barbati/imbracaminte/geci/geci-de-piele-barbati?sort=p.price&order=ASC&limit=110


https://www.readytowear.ro/barbati/imbracaminte/geci/geci-de-piele-barbati/geaca-de-piele-naturala-barbati-gipsy-bleumarin-alb-murdar
locator1 = #content > div.product-info > div.right > div.price
locator2 = span.txt_price
#content > div.product-info > div.right > div.price > br:nth-child(2)

#default_path = 'https://www.gipsy.eu/herren/jacken/lederjacken/2898/gbtroon-2-sf-lacav?number=1677699'
#default_locator_paragraphs = 'span.price--content.content--default'
#default_locator_details = ''
'''


class AppScraper:
    pass



def main():
    from GUI import CreateFieldsButtons

    # Create the entire GUI
    my_GUI = CreateFieldsButtons()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()


    #df = pd.DataFrame({"Field 1" : my_GUI.input1_list, "Field 2" : my_GUI.input2_list, "Field 3" : my_GUI.input3_list}, index=[0])

    # Converting to excel 
    #df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/GUI/Templates_Classes/Output_Excel.xlsx', index = False)



if __name__ == "__main__":
    main()
