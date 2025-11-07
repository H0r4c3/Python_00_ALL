'''
We’ll create another file (evaluator.py) with a class ModelEvaluator. This class will:

Load any saved model from the models/ folder.

Evaluate it on the original Celsius → Fahrenheit dataset (or any test dataset you provide).

Report metrics like Mean Squared Error (MSE) and R² score (common for regression tasks).
'''

import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from save_model import ModelManager
from train_model import CelsiusToFahrenheitModel


class ModelEvaluator:
    """
    Evaluates trained models using test data.
    """

    def __init__(self, model_path):
        self.manager = ModelManager()
        self.model = self.manager.load_model(model_path)

        # Load the same splits as used in training
        self.temp_model = CelsiusToFahrenheitModel()
        self.temp_model.load_data()
        self.X_train, self.X_test, self.y_train, self.y_test = self.temp_model.get_data_splits()

    def evaluate(self):
        """
        Evaluate the model on test data only.
        """
        y_pred = self.model.predict(self.X_test)

        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)

        print("📊 Model Evaluation Results (on Test Set):")
        print(f"  Mean Squared Error (MSE): {mse:.6f}")
        print(f"  R² Score: {r2:.6f}")

        return self.X_test, self.y_test, y_pred
    
    def evaluate_multiple(self):
        """
        Evaluate the model on a few manually chosen Celsius values.
        """
        celsius_test_list = np.array([[-50], [0], [50], [100]])
        fahrenheit_test_correct_list = np.array([[-58.0], [32.0], [122.0], [212.0]])

        fahrenheit_prediction_list = [
            self.model.predict(temperature.reshape(1, -1))[0]
            for temperature in celsius_test_list
        ]

        return celsius_test_list, fahrenheit_test_correct_list, fahrenheit_prediction_list



    def plot_results(self):
        """
        Plot actual vs predicted Fahrenheit values (test set).
        """
        y_pred = self.model.predict(self.X_test)

        plt.figure(figsize=(8, 6))
        plt.scatter(self.X_test, self.y_test, color="blue", label="Actual values")
        plt.scatter(self.X_test, y_pred, color="red", marker="x", label="Predicted values")
        plt.xlabel("Celsius")
        plt.ylabel("Fahrenheit")
        plt.title("Actual vs Predicted Fahrenheit (Test Set)")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_residuals(self):
        """
        Plot residuals (errors = actual - predicted).
        """
        y_pred = self.model.predict(self.X_test)
        residuals = self.y_test - y_pred

        plt.figure(figsize=(8, 6))
        plt.scatter(self.X_test, residuals, color="purple", alpha=0.7)
        plt.axhline(y=0, color="black", linestyle="--", linewidth=1)
        plt.xlabel("Celsius (Test Data)")
        plt.ylabel("Residuals (Actual - Predicted)")
        plt.title("Residuals Plot (Test Set)")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    # Always resolve the models folder relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(script_dir, "models")

    # Find all saved models
    model_files = sorted(glob.glob(os.path.join(models_dir, "*.pkl")))

    if not model_files:
        print("❌ No models found in 'models/' folder.")
    else:
        print("📂 Available models:")
        for idx, file in enumerate(model_files, start=1):
            print(f"{idx}. {os.path.basename(file)}")

        # Let user choose which one to evaluate
        choice = int(input("\n👉 Enter the number of the model to evaluate: "))

        if 1 <= choice <= len(model_files):
            selected_model = model_files[choice - 1]
            print(f"\n🔍 Evaluating: {selected_model}")

            evaluator = ModelEvaluator(selected_model)
            evaluator.evaluate()
            evaluator.plot_results()
            evaluator.plot_residuals()
        else:
            print("❌ Invalid choice.")
            
        celsius_test_list, fahrenheit_test_correct_list, fahrenheit_prediction_list = evaluator.evaluate_multiple()

        print("\n🌡 Celsius | ✅ Expected F | 🤖 Predicted F")
        print("-" * 41)

        for c, f_correct, f_pred in zip(
            celsius_test_list.flatten(),
            fahrenheit_test_correct_list.flatten(),
            fahrenheit_prediction_list
        ):
            print(f"{c:10.1f} | {f_correct:12.1f} | {f_pred:12.1f}")


