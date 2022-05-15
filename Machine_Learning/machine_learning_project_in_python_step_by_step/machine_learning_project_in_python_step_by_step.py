'https://machinelearningmastery.com/machine-learning-in-python-step-by-step/'

'''
In this step-by-step tutorial you will:
Download and install Python SciPy and get the most useful package for machine learning in Python.
Load a dataset and understand it’s structure using statistical summaries and data visualization.
Create 6 machine learning models, pick the best and build confidence that the accuracy is reliable.
'''

'''
The best small project to start with on a new tool is the classification of iris flowers (e.g. the iris dataset).
https://archive.ics.uci.edu/ml/datasets/Iris
Data Set Information:
This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. 
(See Duda & Hart, for example.) The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. 
One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.
Predicted attribute: class of iris plant.
This is an exceedingly simple domain.
This data differs from the data presented in Fishers article (identified by Steve Chadwick, spchadwick '@' espeedaz.net ). 
The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and third features.

Attribute Information:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica
'''

# Check the versions of libraries

# Python version
import sys
#print('Python: {}'.format(sys.version))
# scipy
import scipy
#print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
#print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
#print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas as pd
#print('pandas: {}'.format(pd.__version__))
# scikit-learn
import sklearn
#print('sklearn: {}'.format(sklearn.__version__))


# Load libraries
#from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Load dataset
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
url = r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\0_ALL\Machine_Learning\machine_learning_project_in_python_step_by_step\iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

# We can get a quick idea of how many instances (rows) and how many attributes (columns) the data contains with the shape property:

# shape
print('\nShape: \n', dataset.shape)

# head
print('\nHead: \n', dataset.head(20))

# Now we can take a look at a summary of each attribute.
# This includes the count, mean, the min and max values as well as some percentiles.

# descriptions
print('\nDescription: \n', dataset.describe())

# Let’s now take a look at the number of instances (rows) that belong to each class:

# class distribution
print('\nClass Distribution: \n', dataset.groupby('class').size())

'''
We are going to look at two types of plots:
1. Univariate plots to better understand each attribute.
2. Multivariate plots to better understand the relationships between attributes.
'''

# We start with some univariate plots, that is, plots of each individual variable.

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# We can also create a histogram of each input variable to get an idea of the distribution.

# histograms (It looks like perhaps two of the input variables have a Gaussian distribution. This is useful to note as we can use algorithms that can exploit this assumption.)
dataset.hist()
pyplot.show()

# Now we can look at the interactions between the variables.
# Note the diagonal grouping of some pairs of attributes. This suggests a high correlation and a predictable relationship.

# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()

'''
Now, it is time to create some models of the data and estimate their accuracy on unseen data.
Here is what we are going to cover in this step:
1. Separate out a validation dataset.
2. Set-up the test harness to use 10-fold cross validation.
3. Build multiple different models to predict species from flower measurements
4. Select the best model.
'''

'''
1. Create a Validation Dataset:
We need to know that the model we created is good.
We will split the loaded dataset into two, 80% of which we will use to train, evaluate and select among our models, and 20% that we will hold back as a validation dataset.
'''

# Split-out validation dataset (You now have training data in the X_train and Y_train for preparing models and a X_validation and Y_validation sets that we can use later.)
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

'''
2. Test Harness:
We will use stratified 10-fold cross validation to estimate model accuracy.
This will split our dataset into 10 parts, train on 9 and test on 1 and repeat for all combinations of train-test splits.
Stratified means that each fold or split of the dataset will aim to have the same distribution of example by class as exist in the whole training dataset.
For more on the k-fold cross-validation technique, see the tutorial: https://machinelearningmastery.com/k-fold-cross-validation/
We set the random seed via the random_state argument to a fixed number to ensure that each algorithm is evaluated on the same splits of the training dataset.
We are using the metric of ‘accuracy‘ to evaluate models.
This is a ratio of the number of correctly predicted instances divided by the total number of instances in the dataset multiplied by 100 to give a percentage (e.g. 95% accurate). 
We will be using the scoring variable when we run build and evaluate each model next.
'''

'''
3: Build Models
We don’t know which algorithms would be good on this problem or what configurations to use.
We get an idea from the plots that some of the classes are partially linearly separable in some dimensions, so we are expecting generally good results.
Let’s test 6 different algorithms:
Logistic Regression (LR)
Linear Discriminant Analysis (LDA)
K-Nearest Neighbors (KNN).
Classification and Regression Trees (CART).
Gaussian Naive Bayes (NB).
Support Vector Machines (SVM).
This is a good mixture of simple linear (LR and LDA), nonlinear (KNN, CART, NB and SVM) algorithms.
'''

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

'''
4. Select Best Model:
We now have 6 models and accuracy estimations for each. We need to compare the models to each other and select the most accurate.
Running the example above, we get 6 raw results.

In this case, we can see that it looks like Support Vector Machines (SVM) has the largest estimated accuracy score at about 0.98 or 98%.
We can also create a plot of the model evaluation results and compare the spread and the mean accuracy of each model. There is a population of accuracy 
measures for each algorithm because each algorithm was evaluated 10 times (via 10 fold-cross validation).
A useful way to compare the samples of results for each algorithm is to create a box and whisker plot for each distribution and compare the distributions.
'''

# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

'''
We can see that the box and whisker plots are squashed at the top of the range, with many evaluations achieving 100% accuracy, and some pushing down into the high 80% accuracies.
'''

'''
5. Make Predictions:
We must choose an algorithm to use to make predictions.
The results in the previous section suggest that the SVM was perhaps the most accurate model. We will use this model as our final model.
Now we want to get an idea of the accuracy of the model on our validation set.
This will give us an independent final check on the accuracy of the best model. It is valuable to keep a validation set just in case you made a slip during training, 
such as overfitting to the training set or a data leak. 
Both of these issues will result in an overly optimistic result.
We can fit the model on the entire training dataset and make predictions on the validation dataset.
'''

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

'''
You might also like to make predictions for single rows of data. For examples on how to do that, see the tutorial:
https://machinelearningmastery.com/make-predictions-scikit-learn/

You might also like to save the model to file and load it later to make predictions on new data. For examples on how to do this, see the tutorial:
https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
'''

'''
6. Evaluate Predictions:
We can evaluate the predictions by comparing them to the expected results in the validation set, then calculate classification accuracy, as well as a confusion matrix and a classification report.
'''

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

'''
We can see that the accuracy is 0.966 or about 96% on the hold out dataset.
The confusion matrix provides an indication of the errors made.
Finally, the classification report provides a breakdown of each class by precision, recall, f1-score and support showing excellent results (granted the validation dataset was small).
'''


'''
Looking to continue to practice your machine learning skills, take a look at some of these tutorials:
https://machinelearningmastery.com/start-here/#python
'''