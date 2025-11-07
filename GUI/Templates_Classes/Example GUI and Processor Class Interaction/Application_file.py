from Processor_file import Processor
from GUI_file import GUI

class Application:
    def __init__(self):
        # Create instances of both classes
        # Pass the processor to the GUI
        self.processor = Processor()
        self.gui = GUI(self.processor)
    
    def run(self):
        # Start the application
        self.gui.run()

# Create and run the application
if __name__ == "__main__":
    app = Application()
    app.run()