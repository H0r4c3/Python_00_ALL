# GUI.py
import tkinter as tk

class GUI:
    def __init__(self, text_processor):
        # Instead of creating its own TextProcessor, GUI now receives it as a parameter
        self.text_processor = text_processor
        
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Character Multiplier")
        self.window.geometry("400x300")
        
        # Create and configure the input field
        self.input_label = tk.Label(self.window, text="Enter a character:")
        self.input_label.pack(pady=10)
        
        self.input_field = tk.Entry(self.window)
        self.input_field.pack(pady=5)
        
        # Create the process button
        self.process_button = tk.Button(self.window, text="Process", command=self.process_input)
        self.process_button.pack(pady=10)
        
        # Create the output text area
        self.output_text = tk.Text(self.window, height=10, width=40)
        self.output_text.pack(pady=10)
    
    def process_input(self):
        # Get the input character
        char = self.input_field.get()
        if char:
            # Use the provided text_processor instance to process the input
            result = self.text_processor.multiply_char(char)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, result)
    
    def run(self):
        # Start the main event loop
        self.window.mainloop()

# text_processor.py
class TextProcessor:
    def __init__(self, multiplier=10):
        self.multiplier = multiplier
    
    def multiply_char(self, char):
        """
        Multiplies the input character by the specified multiplier
        Returns the resulting string
        """
        if len(char) > 0:
            # Take only the first character if more than one is entered
            char = char[0]
            return char * self.multiplier
        return ""

# APP.py
from GUI import GUI
from text_processor import TextProcessor

def main():
    # Create an instance of TextProcessor
    text_processor = TextProcessor(multiplier=15)  # We can easily modify the multiplier here
    
    # Create an instance of GUI and pass the TextProcessor instance to it
    gui = GUI(text_processor)
    
    # Start the application
    gui.run()

if __name__ == "__main__":
    main()
