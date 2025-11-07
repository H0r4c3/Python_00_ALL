'ChatGPT'

import webbrowser
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    # Set the browser to Edge
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"))
    webbrowser.get('edge').open("http://127.0.0.1:5000")
    app.run(debug=True)