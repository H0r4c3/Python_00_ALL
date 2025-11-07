from data_processor_file import DataProcessor
from data_gui_file import DataEntryGUI

class Application:
    def __init__(self):
        # Create an instance of DataProcessor to handle data
        self.data_processor = DataProcessor()

        # Create GUI with a callback to process data
        self.gui = DataEntryGUI(self.process_input)

    def process_input(self, input_val1, input_val2, input_val3):
        # Use DataProcessor to process and store values
        self.data_processor.process_values(input_val1, input_val2, input_val3)
            
        # Print the processed values
        self.data_processor.print_values()

    def run(self):
        self.gui.run()

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()