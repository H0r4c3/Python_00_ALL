import tkinter as tk

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
        submit_button = tk.Button(self.window, text="Submit", command=self.submit_data)
        submit_button.pack(pady=10)

    def submit_data(self):
        """
        Collect data from input fields and call the submit callback.
        """
        input_val1 = int(self.entry1.get())
        input_val2 = int(self.entry2.get())
        input_val3 = int(self.entry3.get())
        
        self.submit_callback(input_val1, input_val2, input_val3)

    def run(self):
        self.window.mainloop()
        
