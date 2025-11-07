import tkinter as tk
from printer import Printer

class GuiWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Data Entry")
        
        # Create entry field
        self.entry = tk.Entry(self.window)
        self.entry.pack(pady=10)
        
        # Create button to send data
        self.button = tk.Button(self.window, text="Print Value", command=self.send_to_printer)
        self.button.pack(pady=5)
        
        # Create instance of Printer class
        self.printer = Printer()
        
    def send_to_printer(self):
        # Get value from entry field and send to printer
        value = self.entry.get()
        self.printer.print_value(value)
        
    def run(self):
        self.window.mainloop()