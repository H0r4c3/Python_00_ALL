

#Lesson 3: Load Data From CSV

# Load CSV using Pandas from URL
import pandas
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
url = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Machine_Learning_Mini-Course\pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)

print(data)

# Review the dimensions of your data with the shape property
print(data.shape)

# Review the distribution of your data with the describe() function
description = data.describe()
print(description)

