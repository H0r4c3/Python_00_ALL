'https://www.geeksforgeeks.org/how-to-run-a-flask-application/'

'''
The code you provided is a well-structured and functional Flask application! Here's a breakdown of what each part does:

1. Importing Flask:
from flask import Flask: This line imports the Flask class from the flask module. You'll use this class to create your web application.

2. Creating a Flask App:
app = Flask(__name__): This line creates an instance of the Flask class and assigns it to the variable app. 
The __name__ argument is a special variable that holds the name of the current Python module.   

3. Defining a Route:
@app.route("/"): This line is a decorator that defines a route for your application. The @ symbol applies the decorator to the following function (hello_world). 
The "/" argument specifies that this function will handle requests to the root URL (e.g., http://localhost:5000/).

4. Creating a View Function:
def hello_world(): This function is called a "view function" in Flask. It defines the logic that will be executed when a request is made 
to the route associated with the decorator (/).
return "<p>Hello, World!</p>": This line returns an HTML string with a paragraph element containing the text "Hello, World!". 
This will be displayed in the browser when the root URL is accessed.

5. Running the Application:
if __name__ == '__main__':: This block ensures that the code within it only executes when the script is run directly (not when imported as a module).
app.run(debug=True): This line starts the development server. The debug=True argument enables debug mode, which is helpful for catching errors during development.
'''


# import flask module
from flask import Flask
 
# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
 
if __name__ == '__main__':  
   app.run(debug=True)