'''
There are many excellent standard machine learning datasets in CSV format that you can download and practice with on the UCI machine learning repository:
https://archive.ics.uci.edu/ml/index.php

Practice loading CSV files into Python using the CSV.reader() in the standard library.
Practice loading CSV files using NumPy and the numpy.loadtxt() function.
Practice loading CSV files using Pandas and the pandas.read_csv() function.
'''


# Load CSV using Pandas from URL
import pandas
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Machine_Learning\Machine_learning_mastery_with_python_mini_course\pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(path, names=names)
print(data.shape)