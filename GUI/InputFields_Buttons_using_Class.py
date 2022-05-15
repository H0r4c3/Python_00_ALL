import tkinter as tk

class CreateFieldsButtons():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Window")

        self.create_fields()
        self.create_buttons()

    def create_fields(self):
        tk.Label(self.window, text="First Name").grid(row=0)
        tk.Label(self.window, text="Last Name").grid(row=1)

        self.e1 = tk.Entry(self.window)
        self.e2 = tk.Entry(self.window)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

    def create_buttons(self):
        tk.Button(self.window, text='Quit', command=self.window.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
        tk.Button(self.window, text='Show', command=self.show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

    def show_entry_fields(self):
        print("First Name: %s\nLast Name: %s" % (self.e1.get(), self.e2.get()))



def main():

    # Create the entire GUI
    my_GUI = CreateFieldsButtons()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.window.mainloop()

    #df = pd.DataFrame({"Field 1" : my_GUI.input1_list, "Field 2" : my_GUI.input2_list, index=[0])

    # Converting to excel 
    #df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/GUI/Templates_Classes/Output_Excel.xlsx', index = False)



if __name__ == "__main__":
    main()
