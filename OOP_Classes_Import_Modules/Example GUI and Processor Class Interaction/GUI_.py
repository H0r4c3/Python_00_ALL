import tkinter as tk

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
        self.process_button = tk.Button(self.window, text="Process", command=self.handle_process)
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