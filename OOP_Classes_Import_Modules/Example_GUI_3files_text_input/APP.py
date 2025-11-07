# APP.py

from GUI import GUI
from text_processor import TextProcessor

def main():
    # Create an instance of TextProcessor
    text_processor = TextProcessor()
    
    # Create an instance of GUI and pass the TextProcessor's instance to it
    gui = GUI(text_processor)
    
    # Start the application
    gui.run()

if __name__ == "__main__":
    main()