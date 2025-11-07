'''
f data is small and structured → use scikit-learn (linear/logistic regression, decision trees, etc.).

If data is huge, unstructured (images, text, sound) → use TensorFlow/PyTorch (neural networks).

That’s why for Celsius→Fahrenheit, sklearn is the most practical and elegant solution.

Why did I use sklearn.linear_model.LinearRegression?

Because:

scikit-learn (sklearn) is the go-to library for classical machine learning.

LinearRegression is very simple, fast, and gives you exactly what you need: slope & intercept.

It’s easier to explain and learn from before jumping into heavy frameworks like TensorFlow or PyTorch.

For small structured datasets (numbers in tables, CSV files), sklearn is usually the right tool.
'''

import tensorflow as tf
import numpy as np

# Data
celsius = np.array([-50, 0, 50, 100], dtype=float)
fahrenheit = np.array([-58, 32, 122, 212], dtype=float)

# Model
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),   # ✅ new style Input
    tf.keras.layers.Dense(units=1)
])

# Compile with Adam (safer than SGD here)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
              loss='mean_squared_error')

# Train
model.fit(celsius, fahrenheit, epochs=500, verbose=0)

# Predict
print(model.predict(np.array([[30.0]])))  # should be close to 86°F

# Check learned weights
weights, bias = model.layers[0].get_weights()
print("Weight:", weights, "Bias:", bias)
