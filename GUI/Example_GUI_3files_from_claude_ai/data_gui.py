# data_gui.py
import tkinter as tk
from tkinter import messagebox

class DataEntryGUI:
    """
    A GUI class for entering three values using Tkinter.
    Provides input fields and a method to collect user input.
    """
    def __init__(self, on_submit_callback):
        """
        Initialize the GUI with a callback function for submission.

        Args:
            on_submit_callback (function): Function to call when data is submitted
        """
        self.window = tk.Tk()
        self.window.title("Data Entry Form")
        self.window.geometry("300x250")

        # Callback to be triggered on data submission
        self.submit_callback = on_submit_callback

        # Create input fields
        self.create_input_fields()

    def create_input_fields(self):
        """
        Create and layout input fields for three values.
        Uses labels and entry widgets for user input.
        """
        # Input for first value
        tk.Label(self.window, text="Enter Value 1:").pack(pady=5)
        self.entry1 = tk.Entry(self.window, width=30)
        self.entry1.pack(pady=5)

        # Input for second value
        tk.Label(self.window, text="Enter Value 2:").pack(pady=5)
        self.entry2 = tk.Entry(self.window, width=30)
        self.entry2.pack(pady=5)

        # Input for third value
        tk.Label(self.window, text="Enter Value 3:").pack(pady=5)
        self.entry3 = tk.Entry(self.window, width=30)
        self.entry3.pack(pady=5)

        # Submit button
        submit_btn = tk.Button(self.window, text="Submit", command=self.submit_data)
        submit_btn.pack(pady=10)

    def submit_data(self):
        """
        Collect data from input fields and call the submit callback.
        Validates that all fields are filled before submission.
        """
        val1 = self.entry1.get()
        val2 = self.entry2.get()
        val3 = self.entry3.get()

        # Basic validation to ensure no fields are empty
        if val1 and val2 and val3:
            self.submit_callback(val1, val2, val3)
            messagebox.showinfo("Success", "Data submitted successfully!")
        else:
            messagebox.showerror("Error", "Please fill all fields!")

    def run(self):
        """
        Start the Tkinter event loop to display the GUI.
        """
        self.window.mainloop()
