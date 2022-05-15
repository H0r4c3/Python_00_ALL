import sys

#sys.path.append(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL')

from GUI_for_selecting_a_folder import GUIForSelectingAFolder


def main():
    # Create the GUI
    my_GUI = GUIForSelectingAFolder()
    
    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.root.mainloop()


if __name__ == "__main__":
    main()