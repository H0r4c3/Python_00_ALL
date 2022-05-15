import pandas as pd
import numpy as np
import os

from create_window_for_selecting_paths import CreateMenusFieldsButtons

#path_file1 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/013998-03.hmf"
#path_file2 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/Test_Result03AB.html"
#path_file3 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/What_to_check.txt"

class FileWork:

    def __init__(self, path):
        self.path = path

    def create_list_of_lines(self, path):
        with open(self.path, 'r') as file_reader:
            # Read and print the entire file line by line
            self.list_of_lines = file_reader.read().splitlines() #removes the newline character from the end of every line (/n)
        return self.list_of_lines

    #def find_variable_and_value(self, variable):
        #"""
        #find the variable in every line and make a dictionary with {variable : value}
        #"""
    #    dictionary = {}
    #    for line in self.list_of_lines:
    #        if variable in line:
    #            dictionary[variable] = line.split("=", 1)[-1]
    #    return dictionary

    #def find_variable_and_value(self, list_of_variables):
        #"""
        #find the variable from list_of_variables in every line and make a dictionary with {variable : value}, where 'value' is after "="
        #"""
    #    dictionary = {}
    #    for line in self.list_of_lines:
    #        for variable in list_of_variables:
    #            if variable in line:
    #                dictionary[variable] = line.split("=", 1)[-1]
    #    return dictionary

        

    def find_variable_and_value(self, list_of_variables):
        """
        find the variable from list_of_variables in every line and make a dictionary with {variable : value}, where 'value' is after "="
        """
        dictionary = {}
        dictionary = {line.split("=", 1)[0] : line.split("=", 1)[-1] for line in self.list_of_lines for variable in list_of_variables if variable in line}
        dictionary_without_space_at_end = {key.split(" ", 1)[0] : value.split(" ", 1)[0] for (key, value) in dictionary.items()}
        return dictionary_without_space_at_end



def main():

    # Create the entire GUI program
    my_GUI = CreateMenusFieldsButtons()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()

    print('getcwd:      ', os.getcwd())
    print('__file__:    ', __file__)

    #file1_object = FileWork(path_file1) #HMF file
    #file2_object = FileWork(path_file2) #Report file
    #file3_object = FileWork(path_file3) # What_to_check.txt file (the variables for searching)

    #list_of_lines_file1 = file1_object.create_list_of_lines()
    #list_of_lines_file2 = file2_object.create_list_of_lines()
    #list_of_lines_file3 = file3_object.create_list_of_lines()


    #list_of_variables = ['variable1', 'variable2', 'variable3', 'variable4', 'variable5', 'variable6', 'variable7', 'variable8', 'variable9']
    #list_of_variables = ['PDiag_HellaPartNumValue', 'PDiag_HellaPartAbartValue', 'PDiag_HellaPartNumValue_HellaHWVersionValue', 'PDiag_HellaHWDioCfg', 'PDiag_HellaEVersionValue', 'File', 'HPMVersion', 'CustomerPartNo', 'ZGSVersion', 'EQVersion', 'SupplierPartNo', 'DaimlerHWPartnumber', 'DeviceName', 'HellaSupplierCode']

    #dict3 = file3_object.find_variable_and_value(list_of_lines_file3)
    ##print("Dict3:", dict3)
    #list_of_variables = list(dict3.keys())
    #print('List of variables: ', list_of_variables)

    #dict1 = file1_object.find_variable_and_value(list_of_variables)
    #print(dict1)

    #dict2 = file2_object.find_variable_and_value(list_of_variables)
    #print(dict2)

    # Pass dictionary in Dataframe constructor to create a new object, keys will be in the first column and values in the second column (from the dictionary df1 -> keys : values)
    #df1 = pd.DataFrame.from_dict(my_GUI.compare(), orient = 'index', columns=['hmf_file'])
    #print(df1)

    #df2 = pd.DataFrame.from_dict([dict2], orient = 'columns')
    #df2 = df2.rename(index={0: 'file2'})

    #frames = [df1, df2]
    #df = pd.concat(frames)

    #print(df)

    # first element in df (row=0, column=0)
    #print(df.iloc[0][0])

    #comparison_list = [df.iloc[0][x]==df.iloc[1][x] for x in range(0,9)]
    #print(comparison_list)

    #df.loc[2] = comparison_list
    #df = df.rename(index={2: 'Comparison'})
    #print(df)

    # Converting to excel 
    #df1.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/Comparison.xlsx', index = True)


if __name__ == "__main__":
    main()