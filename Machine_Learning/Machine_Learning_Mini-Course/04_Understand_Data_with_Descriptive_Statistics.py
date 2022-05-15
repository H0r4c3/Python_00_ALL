'''
Understand your data using the head() function to look at the first few rows.
Review the dimensions of your data with the shape property.
Look at the data types for each attribute with the dtypes property.
Review the distribution of your data with the describe() function.
Calculate pairwise correlation between your variables using the corr() function.
'''

# Statistical Summary
import pandas
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
description = data.describe()
print(description)


