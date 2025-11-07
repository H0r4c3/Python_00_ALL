'''
Develop a price prediction algorithm in Python that provides a price for each 50 cryptocurrency pair per voting round. 
The predicted prices should fall within specific target boundaries, between an upper and lower value, which are unknown at prediction time.
'''

'''
Alright, you're in for a fun challenge! Let's get started with an outline for your prediction algorithm. Here's a conceptual approach to get you going:

Gather Data: Collect historical price data for your 50 cryptocurrency pairs.

Preprocess Data: Clean and normalize your data.

Feature Engineering: Create meaningful features like moving averages, volume changes, etc.

Model Selection: Choose and train your prediction model. We can use a simple Linear Regression model, though more sophisticated ones like LSTM (Long Short-Term Memory) could be more accurate.

Define Boundaries: Apply statistical methods to set dynamic upper and lower boundaries for predictions.

Prediction and Voting: Use your trained model to predict prices and adjust based on the predefined boundaries.

Here's a rough skeleton in Python to get you started:
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Step 1: Gather Data
data = pd.read_csv('crypto_prices.csv')  # Load your data here

# Step 2: Preprocess Data
data.fillna(method='ffill', inplace=True)

# Step 3: Feature Engineering
data['MA_5'] = data['Price'].rolling(window=5).mean()
data['MA_20'] = data['Price'].rolling(window=20).mean()
data.dropna(inplace=True)

# Step 4: Model Selection
X = data[['MA_5', 'MA_20']]
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Define Boundaries
def set_boundaries(predictions, factor=0.1):
    lower_bound = predictions * (1 - factor)
    upper_bound = predictions * (1 + factor)
    return lower_bound, upper_bound

# Step 6: Prediction and Voting
predictions = model.predict(X_test)
lower_bound, upper_bound = set_boundaries(predictions)

# Show results
results = pd.DataFrame({'Predicted': predictions, 'Lower': lower_bound, 'Upper': upper_bound})
print(results)

# Voting example:
def voting_round(predictions, lower, upper):
    voted_prices = []
    for i in range(len(predictions)):
        if lower[i] <= predictions[i] <= upper[i]:
            voted_prices.append(predictions[i])
        else:
            voted_prices.append(np.mean([lower[i], upper[i]]))
    return voted_prices

voted_prices = voting_round(predictions, lower_bound, upper_bound)
print(voted_prices)
