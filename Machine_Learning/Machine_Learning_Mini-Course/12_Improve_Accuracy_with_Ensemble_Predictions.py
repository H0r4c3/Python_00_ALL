

# Lesson 12: Improve Accuracy with Ensemble Predictions

# Random Forest Classification
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
num_trees = 100
max_features = 3
kfold = KFold(n_splits=10, random_state=7)
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())

'''
Another way that you can improve the performance of your models is to combine the predictions from multiple models.
Some models provide this capability built-in such as random forest for bagging and stochastic gradient boosting for boosting. Another type of ensembling called 
voting can be used to combine the predictions from multiple different models together.
In today’s lesson, you will practice using ensemble methods.
Practice bagging ensembles with the random forest and extra trees algorithms.
Practice boosting ensembles with the gradient boosting machine and AdaBoost algorithms.
Practice voting ensembles using by combining the predictions from multiple models together.
The snippet below demonstrates how you can use the Random Forest algorithm (a bagged ensemble of decision trees) on the Pima Indians onset of diabetes dataset.
'''
