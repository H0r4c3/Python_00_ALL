'''
Let me help you understand this interaction between GUI and processor classes with a clear example. This is a common pattern in software development that follows the principle of separation of concerns.
GUI and Processor Class Interaction ExampleClick to open code
Let me explain how this works step by step:

First, the Application class acts as the coordinator. When you create an Application instance, it:

Creates a Processor instance
Creates a GUI instance and passes the Processor to it
This establishes the connection between the two classes


In the GUI class initialization:

It receives the Processor instance through its constructor
Stores it as self.processor, making it available throughout the GUI class
Creates the window, entry field, button, and label


When the user interacts with the GUI:

They type text in the entry field
Click the "Process" button
This triggers the handle_process method


The handle_process method shows the full interaction:

Gets the text from the entry field
Calls the Processor's process_text method with this text
Takes the processed result and updates the GUI label



Think of it like a restaurant where:

The Application is the restaurant owner who hires both a waiter (GUI) and a chef (Processor)
The waiter (GUI) takes orders from customers (user input)
The waiter knows about the chef (has the processor instance) and can send orders to them
The chef (Processor) modifies the order (processes the text)
The waiter then delivers the finished dish (processed text) back to the customer

This separation of responsibilities is beneficial because:

The GUI only handles user interaction
The Processor only handles text processing
Neither class needs to know the internal details of how the other works
You can modify either class without affecting the other, as long as their interface stays the same
'''

import tkinter as tk

class Processor:
    def __init__(self):
        # Initialize any processing-related attributes
        self.last_processed = ""
    
    def process_text(self, text):
        # This method modifies the input text (e.g., converts to uppercase)
        self.last_processed = text.upper()
        return self.last_processed

class GUI:
    def __init__(self, processor):
        # The GUI receives an instance of the Processor class
        # This creates a connection between the two classes
        self.processor = processor
        
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Text Processor")
        
        # Create input field
        self.entry = tk.Entry(self.window)
        self.entry.pack(pady=10)
        
        # Create process button
        self.process_button = tk.Button(
            self.window, 
            text="Process", 
            command=self.handle_process
        )
        self.process_button.pack(pady=5)
        
        # Create result label
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack(pady=10)
    
    def handle_process(self):
        # When button is clicked:
        # 1. Get text from entry
        # 2. Send it to processor
        # 3. Update label with result
        input_text = self.entry.get()
        processed_text = self.processor.process_text(input_text)
        self.result_label.config(text=processed_text)
    
    def run(self):
        # Start the GUI event loop
        self.window.mainloop()

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
