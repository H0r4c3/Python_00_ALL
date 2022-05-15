'https://www.geeksforgeeks.org/changing-the-colour-of-tkinter-menu-bar/'

# Import the library tkinter
from tkinter import *
  
# Create a GUI app
app = Tk()
  
# Set the title and geometry to your app
app.title("Geeks For Geeks")
app.geometry("800x500")
  
# Create menubar by setting the color
menubar = Menu(app, background='blue', fg='white')
  
# Declare file and edit for showing in menubar
file = Menu(menubar, tearoff=False, background='yellow')
edit = Menu(menubar, tearoff=False, background='pink')
  
# Add commands in in file menu
file.add_command(label="New")
file.add_command(label="Exit", command=app.quit)
  
# Add commands in edit menu
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
  
# Display the file and edit declared in previous step
menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)
  
# Displaying of menubar in the app
app.config(menu=menubar)
  
# Make infinite loop for displaying app on screen
app.mainloop()
