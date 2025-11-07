# data_processor.py
class DataProcessor:
    """
    A class to process and store three input values.
    This class demonstrates basic data handling with a method to print values.
    """
    def __init__(self):
        """
        Initialize the DataProcessor with None values.
        These will be set when data is processed.
        """
        self.value1 = None
        self.value2 = None
        self.value3 = None

    def process_values(self, val1, val2, val3):
        """
        Store and process the three input values.

        Args:
            val1 (str): First input value
            val2 (str): Second input value
            val3 (str): Third input value
        """
        self.value1 = val1
        self.value2 = val2
        self.value3 = val3

    def print_values(self):
        """
        Print the stored values in a formatted way.
        Demonstrates basic output of processed data.
        """
        print(f"Value 1: {self.value1}")
        print(f"Value 2: {self.value2}")
        print(f"Value 3: {self.value3}")
