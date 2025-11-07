class Processor:
    def __init__(self):
        # Initialize any processing-related attributes
        self.last_processed = ""
    
    def process_text(self, text):
        # This method modifies the input text (e.g., converts to uppercase)
        self.last_processed = text.upper()
        return self.last_processed