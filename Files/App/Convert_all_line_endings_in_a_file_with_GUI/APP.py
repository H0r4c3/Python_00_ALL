

from GUI_for_selecting_a_file import CreateMenusFieldsButtons

def main():
    # Create the entire GUI program
    my_GUI = CreateMenusFieldsButtons()

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.root.mainloop()


if __name__ == "__main__":
    main()