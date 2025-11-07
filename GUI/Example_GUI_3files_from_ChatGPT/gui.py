import tkinter as tk
from tkinter import messagebox

class GUIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Value Input")
        
        # Labels
        tk.Label(self.root, text="Enter Value 1:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Enter Value 2:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Enter Value 3:").grid(row=2, column=0, padx=10, pady=10)
        
        # Entry fields
        self.value1_entry = tk.Entry(self.root)
        self.value2_entry = tk.Entry(self.root)
        self.value3_entry = tk.Entry(self.root)
        self.value1_entry.grid(row=0, column=1, padx=10, pady=10)
        self.value2_entry.grid(row=1, column=1, padx=10, pady=10)
        self.value3_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit).grid(row=3, column=0, columnspan=2, pady=20)
    
    def submit(self):
        value1 = self.value1_entry.get()
        value2 = self.value2_entry.get()
        value3 = self.value3_entry.get()
        
        if not value1 or not value2 or not value3:
            messagebox.showerror("Error", "All fields must be filled!")
        else:
            self.on_submit(value1, value2, value3)

    def on_submit(self, value1, value2, value3):
        pass  # To be implemented in the main app

    def run(self):
        self.root.mainloop()
