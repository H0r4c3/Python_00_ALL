from train_model import CelsiusToFahrenheitModel
from save_model import ModelManager

if __name__ == "__main__":
    # 1️⃣ Train the model
    converter = CelsiusToFahrenheitModel()
    converter.load_data()
    converter.train()
    converter.print_model_parameters()
    
    # 2️⃣ Show slope/intercept (optional)
    model = converter.get_model()
    print(f"Slope (coefficient): {model.coef_[0]}")
    print(f"Intercept: {model.intercept_}")

    # 3️⃣ Save the model
    manager = ModelManager()
    filepath = manager.save_model(converter.model)
    print(f"Model saved at: {filepath}")

    # Load the model back
    loaded_model = manager.load_model(filepath)

    # Test prediction with the loaded model
    prediction = loaded_model.predict([[100]])[0]
    print("Prediction with loaded model (100°C):", prediction)


