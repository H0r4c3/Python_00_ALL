
'''
Boxplots summarize the distribution of each attribute, drawing a line for the median (middle value) 
and a box around the 25th and 75th percentiles (the middle 50% of the data). 
The whiskers give an idea of the spread of the data and dots outside of the whiskers show candidate 
outlier values (values that are 1.5 times greater than the size of spread of the middle 50% of the data).
'''

# Box and Whisker Plots
import matplotlib.pyplot as plt
import pandas
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()
