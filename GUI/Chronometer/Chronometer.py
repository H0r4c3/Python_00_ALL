import tkinter as tk
import time

class ChronometerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chronometer")
        
        self.running = False
        self.start_time = 0
        
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        
        self.start_button.pack()
        self.stop_button.pack()
        self.reset_button.pack()
        
    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.start_time
            self.update()
        
    def stop(self):
        if self.running:
            self.running = False
            self.start_time = time.time() - self.start_time
        
    def reset(self):
        self.running = False
        self.start_time = 0
        self.label.config(text="00:00:00")
        
    def update(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            hours, remainder = divmod(int(elapsed_time), 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.label.config(text=time_str)
            self.label.after(1000, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChronometerApp(root)
    root.mainloop()