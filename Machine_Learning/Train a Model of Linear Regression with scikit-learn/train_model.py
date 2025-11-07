'''
ChatGPG
What this does:

load_data() → loads your Celsius/Fahrenheit pairs.

train() → fits a linear regression model to the data.

print_model_parameters() → prints slope & intercept (should be close to 1.8 and 32).

predict() → predicts Fahrenheit for any Celsius input.

plot_results() → visualizes the data points and the regression line.

👉 This way, you’re treating Celsius-to-Fahrenheit conversion as a learning problem, even though we know the exact formula. 
It’s a great sandbox for understanding how machine learning models “discover” hidden rules.
'''

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class CelsiusToFahrenheitModel:
    """
    Train a linear regression model for Celsius → Fahrenheit conversion.
    """

    def __init__(self):
        self.model = LinearRegression()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.is_trained = False

    def load_data(self):
        """
        Load Celsius → Fahrenheit pairs and split into train and test sets.
        """
        celsius = np.array([
            -50.0, -40.0, -30.0, -20.0, -10.0, -5.0, 0.0, 5.0, 10.0, 15.0,
            20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
            60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 150.0
        ]).reshape(-1, 1)

        fahrenheit = np.array([
            -58.0, -40.0, -22.0, -4.0, 14.0, 23.0, 32.0, 41.0, 50.0, 59.0,
            68.0, 77.0, 86.0, 95.0, 104.0, 113.0, 122.0,
            140.0, 158.0, 176.0, 194.0, 212.0, 230.0, 248.0, 302.0
        ])

        # 80% training, 20% testing
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            celsius, fahrenheit, test_size=0.2, random_state=42
        )

    def train(self):
        """
        Fit the model using the training data.
        """
        if self.X_train is None:
            self.load_data()
        self.model.fit(self.X_train, self.y_train)
        self.is_trained = True
        
    def print_model_parameters(self):
        """Show slope and intercept of the trained model."""
        if not self.is_trained:
            raise Exception("Model is not trained yet!")

        slope = self.model.coef_[0]
        intercept = self.model.intercept_
        print(f"Slope (coefficient): {slope}")
        print(f"Intercept: {intercept}")
    
    
    def predict(self, celsius_value):
        """Predict Fahrenheit for a given Celsius value."""
        if not self.is_trained:
            raise Exception("Model is not trained yet!")

        return self.model.predict(np.array([[celsius_value]]))[0]
    

    def get_data_splits(self):
        """
        Return train/test splits for evaluation.
        """
        return self.X_train, self.X_test, self.y_train, self.y_test

    def get_model(self):
        return self.model
