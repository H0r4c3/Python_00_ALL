import pandas as pd
import numpy as np

path_file1 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/File1.txt"
path_file2 = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/File2.txt"

class FileWork:

    def __init__(self, path):
        self.path = path

    def create_list_of_lines(self):
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
        dictionary = {variable : line.split("=", 1)[-1] for line in self.list_of_lines for variable in list_of_variables if variable in line}
        return dictionary



def main():

    file1_object = FileWork(path_file1)
    file2_object = FileWork(path_file2)

    list_of_lines_file1 = file1_object.create_list_of_lines()
    list_of_lines_file2 = file2_object.create_list_of_lines()

    list_of_variables = ['variable1', 'variable2', 'variable3', 'variable4', 'variable5', 'variable6', 'variable7', 'variable8', 'variable9']

    dict1 = file1_object.find_variable_and_value(list_of_variables)
    print(dict1)

    dict2 = file2_object.find_variable_and_value(list_of_variables)
    print(dict2)

    # Pass dictionary in Dataframe constructor to create a new object, keys will be the column names and value will be column data
    df1 = pd.DataFrame.from_dict([dict1], orient = 'columns')
    df1 = df1.rename(index={0: 'file1'})

    df2 = pd.DataFrame.from_dict([dict2], orient = 'columns')
    df2 = df2.rename(index={0: 'file2'})

    frames = [df1, df2]
    df = pd.concat(frames)

    print(df)

    # first element in df (row=0, column=0)
    #print(df.iloc[0][0])

    comparison_list = [df.iloc[0][x]==df.iloc[1][x] for x in range(0,9)]
    print(comparison_list)

    df.loc[2] = comparison_list
    df = df.rename(index={2: 'Comparison'})
    print(df)

    # Converting to excel 
    df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/Comparison.xlsx', index = True)


if __name__ == "__main__":
    main()