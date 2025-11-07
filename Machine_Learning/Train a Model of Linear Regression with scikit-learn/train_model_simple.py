'''
ChatGPT
'''

import numpy as np
from sklearn.linear_model import LinearRegression

# Datele: Celsius -> Fahrenheit
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

# Creăm și antrenăm modelul
model = LinearRegression()
model.fit(celsius, fahrenheit)

# Afișăm coeficienții
print("Panta (slope):", model.coef_[0])    # ar trebui să fie ~1.8 (adică 9/5)
print("Intercept:", model.intercept_)      # ar trebui să fie ~32

# Testăm: la 100°C ar trebui să dea 212°F
c_test = np.array([[100]])
f_pred = model.predict(c_test)
print("100°C =", f_pred[0], "°F")
