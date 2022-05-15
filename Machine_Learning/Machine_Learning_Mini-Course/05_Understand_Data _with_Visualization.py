

# Scatter Plot Matrix
import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix

url = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Machine_Learning_Mini-Course\pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
scatter_matrix(data)
plt.show()

'''
Today, your lesson is to learn how to use plotting in Python to understand attributes alone and their interactions. Again, I recommend using the helper functions provided on the Pandas DataFrame.

Use the hist() function to create a histogram of each attribute.
Use the plot(kind=’box’) function to create box-and-whisker plots of each attribute.
Use the pandas.scatter_matrix() function to create pairwise scatterplots of all attributes.
'''
