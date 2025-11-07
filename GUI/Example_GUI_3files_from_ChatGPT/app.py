from printer import ValuePrinter
from gui import GUIApp

class App:
    def __init__(self):
        self.gui = GUIApp()
        self.printer = ValuePrinter()

        # Override the on_submit method
        self.gui.on_submit = self.handle_submission

    def handle_submission(self, value1, value2, value3):
        # Use the ValuePrinter class to print the values
        self.printer.print_values(value1, value2, value3)

    def run(self):
        self.gui.run()

if __name__ == "__main__":
    app = App()
    app.run()
