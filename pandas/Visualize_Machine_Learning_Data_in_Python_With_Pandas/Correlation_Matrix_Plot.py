'''
Correlation gives an indication of how related the changes are between two variables. 
If two variables change in the same direction they are positively correlated. 
If the change in opposite directions together (one goes up, one goes down), then they are negatively correlated.
You can calculate the correlation between each pair of attributes. This is called a correlation matrix. 
You can then plot the correlation matrix and get an idea of which variables have a high correlation with each other.
This is useful to know, because some machine learning algorithms like linear and logistic regression can have poor performance if there are highly correlated input variables in your data.
'''

# Correction Matrix Plot
import matplotlib.pyplot as plt
import pandas
import numpy
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
correlations = data.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()
