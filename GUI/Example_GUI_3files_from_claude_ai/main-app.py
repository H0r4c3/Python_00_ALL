# main.py
from data_processor import DataProcessor
from data_gui import DataEntryGUI

class Application:
    """
    Main application class that connects the DataProcessor and DataEntryGUI.
    Demonstrates composition and interaction between different components.
    """
    def __init__(self):
        """
        Initialize the application by creating instances of 
        DataProcessor and DataEntryGUI.
        """
        # Create an instance of DataProcessor to handle data
        self.data_processor = DataProcessor()

        # Create GUI with a callback to process data
        self.gui = DataEntryGUI(self.process_input)

    def process_input(self, val1, val2, val3):
        """
        Callback method to process input from GUI.
        Calls the DataProcessor to handle the input values.

        Args:
            val1 (str): First input value
            val2 (str): Second input value
            val3 (str): Third input value
        """
        # Use DataProcessor to process and store values
        self.data_processor.process_values(val1, val2, val3)
        
        # Print the processed values
        self.data_processor.print_values()

    def run(self):
        """
        Start the application by running the GUI.
        """
        self.gui.run()

def main():
    """
    Entry point of the application.
    Creates and runs the main application.
    """
    app = Application()
    app.run()

if __name__ == "__main__":
    main()
