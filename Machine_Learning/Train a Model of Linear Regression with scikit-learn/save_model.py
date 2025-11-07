'''
By default, os.makedirs("models") will create the folder relative to wherever you run the script from. 
If you want it to always save in the models/ folder next to the script file (not depending on where you run python), 
you should anchor the path to the script’s directory with __file__.
'''

import os
import joblib
from datetime import datetime

class ModelManager:
    """
    Handles saving and loading machine learning models.
    Models are always saved inside a 'models/' folder
    located in the same directory as this script.
    """

    def __init__(self, save_dir="models"):
        # Find the absolute path to the current script's folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Build the models folder path inside the script's folder
        self.save_dir = os.path.join(script_dir, save_dir)
        
        # Create the folder if it doesn't exist
        os.makedirs(self.save_dir, exist_ok=True)

    def save_model(self, model, base_name="celsius_to_fahrenheit"):
        """
        Save a trained model with a timestamped filename to avoid overwriting.
        Example: models/celsius_to_fahrenheit_2025-08-31_15-45-12.pkl
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{base_name}_{timestamp}.pkl"
        filepath = os.path.join(self.save_dir, filename)

        joblib.dump(model, filepath)
        print(f"✅ Model saved to {filepath}")
        return filepath

    def load_model(self, filepath):
        """
        Load a previously saved model.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"❌ Model file not found: {filepath}")

        model = joblib.load(filepath)
        print(f"✅ Model loaded from {filepath}")
        return model
