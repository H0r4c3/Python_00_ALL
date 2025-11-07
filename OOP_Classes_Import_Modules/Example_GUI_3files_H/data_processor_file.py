class DataProcessor:
    def __init__(self):
        self.input_val1 = None
        self.input_val2 = None
        self.input_val3 = None

    def process_values(self, input_val1, input_val2, input_val3):
        self.sum1 = input_val1 + 1
        self.sum2 = input_val2 + 2
        self.sum3 = input_val3 + 3

    def print_values(self):
        print(f"Value 1: {self.sum1}")
        print(f"Value 2: {self.sum2}")
        print(f"Value 3: {self.sum3}")