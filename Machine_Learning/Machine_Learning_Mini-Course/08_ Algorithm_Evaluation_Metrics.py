

# Cross Validation Classification LogLoss
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression(solver='liblinear')
scoring = 'neg_log_loss'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("Logloss: %.3f (%.3f)") % (results.mean(), results.std())

'''
There are many different metrics that you can use to evaluate the skill of a machine learning algorithm on a dataset.
You can specify the metric used for your test harness in scikit-learn via the cross_validation.cross_val_score() function and defaults can be used for 
regression and classification problems. Your goal with today’s lesson is to practice using the different algorithm performance metrics available in the scikit-learn package.
Practice using the Accuracy and LogLoss metrics on a classification problem.
Practice generating a confusion matrix and a classification report.
Practice using RMSE and RSquared metrics on a regression problem.
The snippet below demonstrates calculating the LogLoss metric on the Pima Indians onset of diabetes dataset.
'''
