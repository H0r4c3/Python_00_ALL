'Split a line of text in lines of equal characters'

from textwrap import wrap

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Strings\file.txt'

with open (path, 'r') as file:
    #print(file.readlines())
    lines = file.readlines()
    long_line = lines[4]

    short_lines_list = wrap(long_line, 180)
    for item in short_lines_list:
        print(item)
    
